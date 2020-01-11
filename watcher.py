"""
script will check for updates on a the template file and will fire off 
the the scripts to add the updated file to the data base
"""
import os.path, time
import sys
from result_processing.execute import execute_process

def terminate_watcher(log_times):
    start = log_times["script_start"]
    end = log_times["terminate_time"]
    print("\nWatcher has exceeded the amount of time, and has been terminated ")
    print(f"Script started: {start}")
    print(f"Script ended: {end}")
    sys.exit()



def main():
    # create a json/ csv setup file for any info
    file = r"result_templates/new_model_template.csv"
    database_file = r"/sql_temp.db"

    file_name = file.split("/")[1]

    start_time = time.time()
    accrued_time = None
    last_checked_time = None
    running = True

    while running:
        update_on_file = os.path.getmtime(file)

        if last_checked_time == None:
            print(f"watching for update on {file_name}")
            print("CNTRL + c, to kill")
            last_checked_time = time.time()

        elif update_on_file <= last_checked_time:
            time.sleep(2)
            accrued_time = time.time()

            time_past = accrued_time - start_time
            print(f"watching for updates {str(round(time_past))} seconds")
            
            if time_past == 720:
                log_times = {
                    "script_start" : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)),
                    "terminate_time" : time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
                }
                terminate_watcher(log_times)
            else: # not sure if need??
                pass
        else:
            print("Template has been update, generate result")
            execute_process(file,database_file)
            last_checked_time = time.time()

if __name__ == "__main__":
    main()



