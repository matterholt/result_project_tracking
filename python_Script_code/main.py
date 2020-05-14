from pkg.execute import execute_process
import os.path


def main():

    file = os.path.join("Templates_csv", "new_model_template.csv")
    database_file = os.path.join("Results", "XYZ_project.db")
    execute_process(file, database_file)


if __name__ == "__main__":
    main()
