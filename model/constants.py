class Paths:
    data_dir = ".../data"
    data_csv = f"{data_dir}/data.csv"
    filtered_csv = f"{data_dir}/filtered.csv"
    segments_dir = f"{data_dir}/segments"
    segment_csv = segments_dir + "/segment_{}.csv"

class Headers:
    headers = {
        "RequestID": str,
        "Boro": str,
        "Yr": str,
        "M": str,
        "D": str,
        "HH": str,
        "MM": str,
        "Vol": str,
        "SegmentID": str,
        "WktGeom": str,
        "street": str,
        "fromSt": str,
        "toSt": str,
        "Direction": str
    }

    garbage_headers = [
        "RequestID",
        "Boro",
        "WktGeom",
        "street",
        "fromSt",
        "toSt",
        "Direction"
    ]

    needed_headers = {
        "Yr": int,
        "M": int,
        "D": int,
        "HH": int,
        "MM": int,
        "Vol": int,
        "SegmentID": int,
    }

class Constants:
    categories = ["Yr", "M", "D", "HH", "MM"]
