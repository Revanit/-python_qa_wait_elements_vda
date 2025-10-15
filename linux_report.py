import subprocess
from datetime import datetime


def parse_ps_aux():
    result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    processes = []
    for line in lines[1:]:
        parts = line.split(None, 10)
        if len(parts) < 11:
            continue
        proc = {
            'USER': parts[0],
            'PID': parts[1],
            '%CPU': float(parts[2]),
            '%MEM': float(parts[3]),
            'VSZ': parts[4],
            'RSS': parts[5],
            'COMMAND': parts[10],
        }
        processes.append(proc)
    return processes


def print_process_list(processes, limit=20):
    """Выводит таблицу активных процессов."""
    print("Список запущенных процессов (топ по памяти):")
    print(f"{'USER':<10} {'PID':<7} {'%CPU':<6} {'%MEM':<6} {'VSZ':<8} {'RSS':<8} COMMAND")
    print("-" * 80)
    sorted_by_mem = sorted(processes, key=lambda x: x['%MEM'], reverse=True)[:limit]
    for p in sorted_by_mem:
        cmd = p['COMMAND'] if len(p['COMMAND']) <= 35 else p['COMMAND'][:32] + "..."
        print(f"{p['USER']:<10} {p['PID']:<7} {p['%CPU']:<6.1f} {p['%MEM']:<6.1f} {p['VSZ']:<8} {p['RSS']:<8} {cmd}")
    print()


def generate_report(processes):
    """Формирует текст отчёта о состоянии системы."""
    users = sorted(set(p['USER'] for p in processes))
    total_processes = len(processes)
    user_proc_count = {}
    for p in processes:
        user_proc_count[p['USER']] = user_proc_count.get(p['USER'], 0) + 1
    total_cpu = sum(p['%CPU'] for p in processes)
    total_mem = sum(p['%MEM'] for p in processes)
    top_mem = max(processes, key=lambda x: x['%MEM'])
    top_cpu = max(processes, key=lambda x: x['%CPU'])

    def shorten(name):
        return name if len(name) <= 30 else name[:27] + "..."
    report = []
    report.append("Отчёт о состоянии системы:")
    report.append(f"Пользователи системы: {', '.join(users)}")
    report.append(f"Процессов запущено: {total_processes}\n")
    report.append("Пользовательских процессов:")
    for user, count in sorted(user_proc_count.items(), key=lambda x: x[1], reverse=True):
        report.append(f"{user}: {count}")
    report.append("")
    report.append(f"Всего памяти используется: {total_mem:.1f}%")
    report.append(f"Всего CPU используется: {total_cpu:.1f}%")
    report.append(f"Больше всего памяти использует: {shorten(top_mem['COMMAND'])} ({top_mem['%MEM']}%)")
    report.append(f"Больше всего CPU использует: {shorten(top_cpu['COMMAND'])} ({top_cpu['%CPU']}%)")
    return '\n'.join(report)

def save_report(report_text):
    """Сохраняет отчёт в txt файл."""
    now = datetime.now().strftime("%d-%m-%Y-%H:%M")
    filename = f"{now}-scan.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report_text)
    return filename


def main():
    processes = parse_ps_aux()

    print_process_list(processes)

    report = generate_report(processes)
    print(report)

    filename = save_report(report)
    print(f"\nОтчёт сохранён в файл: {filename}")


if __name__ == "__main__":
    main()
