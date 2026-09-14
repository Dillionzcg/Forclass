import os
import time

def main():
    target = "report.txt"
    stats_target = "stats.txt"
    
    # 检查 data.csv 或 stats.py 是否更新过
    stats_dep = ["data.csv", "stats.py"]
    report_dep = ["build_report.py", "stats.txt", "report.md"]
    
    need_stats = not os.path.exists(stats_target) or any(
        os.path.getmtime(dep) > os.path.getmtime(stats_target) for dep in stats_dep if os.path.exists(dep)
    )
    
    if need_stats:
        print("Running stats.py...")
        import stats
    else:
        print("stats.txt is up to date.")
        
    need_report = not os.path.exists(target) or any(
        os.path.getmtime(dep) > os.path.getmtime(target) for dep in report_dep if os.path.exists(dep)
    )
    
    if need_report:
        print("Running build_report.py...")
        import build_report
    else:
        print("report.txt is up to date.")

if __name__ == "__main__":
    main()
