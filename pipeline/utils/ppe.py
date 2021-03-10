from passporteye import read_mrz
# Argument can be a path or a file
def read_info(path):
    results = read_mrz(path).to_dict()
    if results:
        print(results)
        return results
    else:
        return "Could not be processed"

