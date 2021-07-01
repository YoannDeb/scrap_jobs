from csv_management.csv_management import create_csv


def filter_by_category(csv_headers, lists_of_all_information):
    """Filter jobs by category and creates a csv file for each category.
    :param csv_headers: headers of the csv file.
    :param lists_of_all_information: list of all information in the origin csv file.
    """
    list_of_categories = [
        "Data_Analyst", "Developer_Engineer", "Manager_Executive",
        "Other", "Researcher_Scientist"
    ]
    for category in list_of_categories:
        lists_of_jobs_in_category = []
        for job in lists_of_all_information:
            if category[:4] in job[8]:
                lists_of_jobs_in_category.append(job)
        if lists_of_jobs_in_category:
            create_csv(
                "sorted_by_category", f"Category_{category}.csv",
                csv_headers, lists_of_jobs_in_category
            )


def filter_by_type(csv_headers, lists_of_all_information):
    """Filter jobs by type and creates a csv file for each type.

    :param csv_headers: headers of the csv file
    :param lists_of_all_information: list of all information
    in the origin csv file
        """
    list_of_types = [
        'Back end', 'Big Data', 'Cloud', 'Database', 'Evangelism', 'Finance',
        'Front end', 'Fundraising', 'Image Processing', 'Integration', 'Lead',
        'Machine Learning', 'Management', 'Numeric processing', 'Operations',
        'Systems', 'Testing', 'Text Processing', 'Web'
    ]
    for job_type in list_of_types:
        lists_of_jobs_in_types = []
        for job in lists_of_all_information:
            if job_type in job[7]:
                lists_of_jobs_in_types.append(job)
        if lists_of_jobs_in_types:
            filename_job_type = job_type.replace(" ", "_")
            create_csv(
                "sorted_by_type", f"Type_{filename_job_type}.csv",
                csv_headers, lists_of_jobs_in_types
            )
