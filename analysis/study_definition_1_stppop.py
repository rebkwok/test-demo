# LIBRARIES

# cohort extractor
from cohortextractor import StudyDefinition, patients

# set the index date
index_date = "2020-01-01"

# STUDY POPULATION

study = StudyDefinition(
    default_expectations={
        "date": {
            "earliest": index_date,
            "latest": "today",
        },  # date range for simulated dates
        "rate": "uniform",
        "incidence": 1,
    },
    # This line defines the study population
    population=patients.registered_as_of(index_date),
    # this line defines the stp variable we want to extract
    stp=patients.registered_practice_as_of(
        index_date,
        returning="stp_code",
        return_expectations={
            "category": {"ratios": {"STP1": 0.3, "STP2": 0.2, "STP3": 0.5}},
        },
    ),
)
