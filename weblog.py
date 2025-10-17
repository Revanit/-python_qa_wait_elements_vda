import os
import json
from collections import Counter


def process_current_directory():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    found_files = []
    for root, _, files in os.walk(current_dir):
        for f in files:
            if f == "access.log":
                found_files.append(os.path.join(root, f))
    if not found_files:
        print("Файл access.log не найден.")
        return
    for file_path in found_files:
        print(f"\nОбрабатываю лог: {file_path}")
        process_log_file(file_path)


def process_log_file(file_path):
    total_requests = 0
    methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"]
    methods_count = {m: 0 for m in methods}
    ip_counter = Counter()
    longest_requests = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total_requests += 1
            parts = line.split()
            if len(parts) < 12:
                continue
            ip = parts[0]
            ip_counter[ip] += 1
            try:
                request_section = line.split('"')[1]
                method, url, protocol = request_section.split()
            except ValueError:
                method, url = "-", "-"
            if method in methods_count:
                methods_count[method] += 1
            try:
                date = "[" + line.split("[")[1].split("]")[0] + "]"
            except IndexError:
                date = "-"
            try:
                duration = int(parts[-1])
            except ValueError:
                duration = 0
            longest_requests.append({
                "ip": ip,
                "date": date,
                "method": method,
                "url": url,
                "duration": duration
            })

    top_ips = dict(ip_counter.most_common(3))
    top_longest = sorted(longest_requests, key=lambda x: x["duration"], reverse=True)[:3]
    result = {
        "top_ips": top_ips,
        "top_longest": top_longest,
        "total_stat": methods_count,
        "total_requests": total_requests
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    output_path = f"{file_path}.json"
    with open(output_path, "w", encoding="utf-8") as out:
        json.dump(result, out, indent=2, ensure_ascii=False)
    print(f"Статистика сохранена в: {output_path}")


if __name__ == "__main__":
    process_current_directory()




