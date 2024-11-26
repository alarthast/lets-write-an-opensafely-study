from ehrql import create_dataset, codelist_from_csv, debug
from ehrql.tables.tpp import patients, clinical_events,practice_registrations, medications

dataset = create_dataset()

index_date = "2020-03-31"

has_registration = practice_registrations.for_patient_on(
    index_date
).exists_for_patient()

dataset.define_population(has_registration)

cake_codes = codelist_from_csv('local-codelists/cake.csv', column="code")
sports_codes = codelist_from_csv('local-codelists/extreme-sports.csv', column='code')

dataset.has_had_cake = medications.where(medications.dmd_code.is_in(cake_codes)).exists_for_patient()
dataset.num_cake_prescriptions = medications.where(medications.dmd_code.is_in(cake_codes)).count_for_patient()

dataset.has_died = patients.is_dead_on(index_date)
dataset.date_of_death = patients.date_of_death

latest_sports_event = clinical_events.where(clinical_events.snomedct_code.is_in(sports_codes)).sort_by(clinical_events.date).last_for_patient()

dataset.latest_sports_date = latest_sports_event.date
dataset.latest_sports_code = latest_sports_event.snomedct_code

debug(dataset)