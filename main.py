from pkg.execute import execute_process


def main():
    
    file = r"Templates_csv/new_model_template.csv"
    database_file = "XYZ_project.db"
    execute_process(file, database_file)


if __name__ == "__main__":
    main()
