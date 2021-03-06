import base64
import re
from io import BytesIO
from typing import Dict, List, Optional
from zipfile import ZipFile

from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from Crypto.Cipher import AES
from loguru import logger

KEY = base64.decodebytes("MkXOl0e30PeWG01t7cTKjA==".encode())


def extract_zip(input_zip) -> Dict[str, bytes]:
    input_zip = ZipFile(input_zip)
    return {name: input_zip.read(name) for name in input_zip.namelist()}


def parse_apk(path: str) -> Optional[APK]:
    try:
        apk = APK(path)
        return apk
    except Exception as e:
        logger.error(f"Failed to parse as an apk: {e}")
        return None


def decrypt_dex(data: bytes) -> Optional[DalvikVMFormat]:
    try:
        aes = AES.new(KEY)
        decrypted = aes.decrypt(data)
        zipfile = BytesIO(decrypted)
        zip_dict = extract_zip(zipfile)
        dex = zip_dict.get("classes.dex")
        if dex is None:
            return None
        return DalvikVMFormat(dex)
    except Exception as e:
        logger.error(f"Failed to decrypt: {e}")
        return None


def find_hidden_dex(apk: APK) -> Optional[DalvikVMFormat]:
    files = apk.get_files()
    hidden_dex_names = [x for x in files if re.match(r"assets/[a-zA-Z0-9]+", x)]
    if len(hidden_dex_names) == 1:
        hidden_dex_name = hidden_dex_names[0]
        data = apk.get_file(hidden_dex_name)
        return decrypt_dex(data)

    return None


def find_urls(strings: List[str]) -> List[str]:
    return [x for x in strings if re.match(r"http[s]?:\/\/[a-zA-Z0-1\.-]+\/", x)]


def find_c2(urls: List[str]) -> List[str]:
    white_list = [
        "http://nittsu-si.com/",
        "http://schemas.android.com/apk/res/android",
        "http://www.sagawa-exp.co.jp/",
    ]
    return list(set(urls) - set(white_list))


def analyze(
    path: str, extract_dex: bool = False, verbose: bool = False
) -> Optional[dict]:
    apk = parse_apk(path)
    if apk is None:
        return None

    dex = find_hidden_dex(apk)
    if dex is None:
        return None

    if extract_dex:
        filename = f"{path}.dex"
        with open(filename, "wb") as fp:
            fp.write(dex.get_buff())
            logger.info(f"A hidden dex is extracted as {filename}")

    strings = [string for string in dex.get_strings()]
    urls = find_urls(strings)
    c2 = find_c2(urls)

    output = {}
    output["c2"] = c2
    if verbose:
        output["hardcoded_urls"] = urls

    return output
