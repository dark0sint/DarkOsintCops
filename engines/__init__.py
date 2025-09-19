from darkosintcops.engines.hiddenwiki import HiddenWikiEngine
from darkosintcops.engines.darksearch import DarkSearchEngine

def get_engines():
    return {
        "hiddenwiki": HiddenWikiEngine(),
        "darksearch": DarkSearchEngine(),
        # Tambahkan mesin pencari lain di sini
    }
