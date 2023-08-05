import time
from typing import Dict, List, Tuple

import requests

from mwconstants.constants.c_languages import WIKIPEDIA_LANGUAGES
from mwconstants.constants.c_namespaces import DEFAULT_NAMESPACES, NAMESPACE_ALIASES
from mwconstants.languages import get_wiki_sites


def get_all_namespace_prefix_map(
    lang: str, project: str = "wikipedia"
) -> Dict[str, dict]:
    """Get mapping of namespaces to canonical / possible aliases for a given wiki.

    For return dictionary:
    * Keys are the local names -- i.e. the official names used in parsed article HTML
    * Values include the canonical name -- e.g., User for fr:Utilisateur
    * Values include the list of possible aliases -- e.g., Utilisatrice
    * Together, the key + canonical + aliases make all the valid prefixes for a namespace

    More details: https://www.mediawiki.org/wiki/Help:Namespaces#Localisation

    NOTE: this data can alternatively be extracted from another dump:
    <lang>-<date>-siteinfo-namespaces.json.gz
    """
    session = requests.Session()
    base_url = f"https://{lang}.{project}.org/w/api.php"
    params = {
        "action": "query",
        "meta": "siteinfo",
        "siprop": "namespaces|namespacealiases",
        "format": "json",
        "formatversion": "2",
    }
    result = session.get(url=base_url, params=params).json()

    prefixes = {}
    id_to_name = {}  # e.g., 1 -> Talk; needed for namespace aliases
    if "namespaces" in result.get("query", {}):
        for ns in result["query"]["namespaces"].values():
            try:
                canonical = ns["canonical"]
                name = ns["name"]
                nid = ns["id"]
                id_to_name[nid] = name
                prefixes[name] = {"canonical": canonical}
            except KeyError:  # main namespace has no canonical prefix and we want to skip it
                continue
    if "namespacealiases" in result.get("query", {}):
        for alias in result["query"]["namespacealiases"]:
            try:
                nid = alias["id"]
                prefix = alias["alias"]
                name = id_to_name[nid]
                prefixes[name]["aliases"] = prefixes[name].get("aliases", []) + [prefix]
            except KeyError:
                print(f"Invalid alias: {alias}")

    return prefixes


def gather_all_languages(
    deduplicate: bool = True,
) -> Tuple[Dict[str, List[str]], Dict[str, dict]]:
    """Helper function for gathering namespace data of a given type."""
    wiki_languages = get_wiki_sites("wiki")
    print(f"{len(wiki_languages)} languages: {wiki_languages}")
    namespaces = {}
    for lang in wiki_languages:
        namespaces[lang] = get_all_namespace_prefix_map(lang, "wikipedia")
        time.sleep(0.25)

    def_ns = {}
    # make sure to copy values not pointers so it's not later removed with English
    for ns_name in namespaces["en"]:
        canonical = namespaces["en"][ns_name]["canonical"]
        if ns_name == canonical:
            aliases = list(namespaces["en"][ns_name].get("aliases", []))
        else:
            aliases = list(
                set(namespaces["en"][ns_name].get("aliases", []) + [ns_name])
            )
        def_ns[canonical] = aliases

    if deduplicate:
        langs_to_remove = []
        for lang in namespaces:
            ns_to_remove = []
            for ns_name in namespaces[lang]:
                ns_prefixes = namespaces[lang][ns_name]
                canonical = ns_prefixes["canonical"]
                if canonical not in def_ns:
                    # Special namespaces that don't appear in English: remove duplicate canonical if relevant
                    if ns_name == canonical:
                        ns_prefixes.pop("canonical")
                    continue
                # remove official aliases that match any default prefixes (canonical/aliases)
                def_prefixes = [canonical] + def_ns[canonical]
                for i in range(len(ns_prefixes.get("aliases", [])) - 1, -1, -1):
                    if ns_prefixes["aliases"][i] in def_prefixes:
                        ns_prefixes["aliases"].pop(i)
                if "aliases" in ns_prefixes and not ns_prefixes["aliases"]:
                    ns_prefixes.pop("aliases")
                # only keep canonical if different from name
                if ns_name == canonical:
                    ns_prefixes.pop("canonical")
                if not ns_prefixes:
                    ns_to_remove.append(ns_name)

            for ns_name in ns_to_remove:
                namespaces[lang].pop(ns_name)
            if not namespaces[lang]:
                langs_to_remove.append(lang)

        for lang in langs_to_remove:
            namespaces.pop(lang)

    return def_ns, namespaces


def standardize_prefix(prefix: str) -> str:
    """Standardize link format"""
    return prefix.split(":", maxsplit=1)[0].replace(" ", "_").capitalize()


def prefixes_to_canonical(
    lang: str = "en", interlanguage: bool = True
) -> Dict[str, str]:
    """Build map of prefixes to their canonical namespace prefix.

    NOTE: the use of standardize_prefix is to ensure look-ups in this dictionary are successful
    but it also makes the dictionary look funny because of the enforced capitalize/underscore style
    """
    if interlanguage:
        prefixes = {
            standardize_prefix(wiki_lang): "Interlanguage"
            for wiki_lang in WIKIPEDIA_LANGUAGES
            if wiki_lang != lang
        }
    else:
        prefixes = {}
    for canonical_ns in DEFAULT_NAMESPACES:
        prefixes[standardize_prefix(canonical_ns)] = canonical_ns
        for alias in DEFAULT_NAMESPACES[canonical_ns]:
            prefixes[standardize_prefix(alias)] = canonical_ns

    for ns in NAMESPACE_ALIASES.get(lang, {}):
        canonical = NAMESPACE_ALIASES[lang][ns].get("canonical", ns)
        prefixes[standardize_prefix(ns)] = canonical
        prefixes[standardize_prefix(canonical)] = canonical
        for alias in NAMESPACE_ALIASES[lang][ns].get("aliases", []):
            prefixes[standardize_prefix(alias)] = canonical

    return prefixes


def get_language_list_prefixes(namespace: str, lang: str) -> List[str]:
    """Generate a list of acceptable prefixes for a particular language+namespace.

    For example: get_language_list_prefixes('File', lang='fr') -> ['Fichier', 'File', 'Image']
    Most useful when working with wikitext where these prefixes would all be valid.
    If working with parsed HTML, only the local language prefix will be used. If checking
    for containment, make sure to standardize both the prefixes and input e.g., via standardize_prefix
    so that e.g., FILE correctly matches against File.
    """

    # try to canonicalize the namespace
    if namespace not in DEFAULT_NAMESPACES:
        for lang_ns in NAMESPACE_ALIASES.get(lang, {}):
            # matches local name, canonical, or an alias
            if (
                namespace == lang_ns
                or namespace == NAMESPACE_ALIASES[lang][lang_ns].get("canonical")
                or namespace in NAMESPACE_ALIASES[lang][lang_ns].get("aliases", [])
            ):
                namespace = NAMESPACE_ALIASES[lang][lang_ns].get("canonical", lang_ns)

    # extract default namespace prefixes
    lang_ns_prefixes = []
    if namespace in DEFAULT_NAMESPACES:
        lang_ns_prefixes.append(namespace)
        lang_ns_prefixes.extend(DEFAULT_NAMESPACES[namespace])

    # add language-specific prefixes
    for lang_ns in NAMESPACE_ALIASES.get(lang, {}):
        if (
            lang_ns == namespace
            or NAMESPACE_ALIASES[lang][lang_ns].get("canonical", None) == namespace
        ):
            lang_ns_prefixes.append(lang_ns)
            canonical_ns = NAMESPACE_ALIASES[lang][lang_ns].get("canonical", None)
            if canonical_ns:
                lang_ns_prefixes.append(canonical_ns)
            lang_ns_prefixes.extend(NAMESPACE_ALIASES[lang][lang_ns].get("aliases", []))

    if not lang_ns_prefixes:
        print(
            f"No results. Maybe because namespace ({namespace}) non-standard: {list(DEFAULT_NAMESPACES.keys())}"
        )
        return []
    else:
        return list(set(lang_ns_prefixes))


if __name__ == "__main__":
    (
        default_namespaces,
        namespace_aliases,
    ) = gather_all_languages()  # Wikipedia namespaces
    print(default_namespaces)
    print(namespace_aliases)
