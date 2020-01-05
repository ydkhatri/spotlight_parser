try:
    import lzfse
    lzfse_capable = True
except ImportError:
    print("lzfse not found. Won't decompress lzfse/lzvn streams")


with open('P:\\temp\\.store_53268_11807.lzfse.db', 'rb') as f:
    comp = f.read()
    decomp = lzfse.decompress(comp)

    print(len(decomp))