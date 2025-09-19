import multiprocessing
from darkosintcops.engines import get_engines
from darkosintcops.utils import write_output

class DarkOsintCopsCore:
    def __init__(self, proxy, output, continuous_write, limit, engines, exclude, fields, field_delimiter, mp_units):
        self.proxy = proxy
        self.output = output
        self.continuous_write = continuous_write
        self.limit = limit
        self.fields = fields
        self.field_delimiter = field_delimiter
        self.mp_units = mp_units or multiprocessing.cpu_count()

        all_engines = get_engines()
        if engines:
            self.engines = {k: v for k, v in all_engines.items() if k in engines}
        elif exclude:
            self.engines = {k: v for k, v in all_engines.items() if k not in exclude}
        else:
            self.engines = all_engines

    def search(self, query):
        print(f"Starting search for: {query}")
        pool = multiprocessing.Pool(self.mp_units)
        results = []

        def collect_result(res):
            results.extend(res)
            if self.continuous_write and self.output:
                write_output(res, self.output, self.fields, self.field_delimiter, append=True)

        jobs = []
        for name, engine in self.engines.items():
            job = pool.apply_async(engine.search, args=(query, self.limit, self.proxy), callback=collect_result)
            jobs.append(job)

        for job in jobs:
            job.wait()

        pool.close()
        pool.join()

        if self.output and not self.continuous_write:
            write_output(results, self.output, self.fields, self.field_delimiter)

        print(f"Search completed. Found {len(results)} results.")
        return results
