worker_age=int(input('Enter workers current age: '))
years_of_service=int(input('Enter workers current years of service: '))
income_1=int(input('Enter the expected largest income: '))
income_2=int(input('Enter the expected second-largest income: '))
income_3=int(input('Enter the expected third-largest income: '))

rate=0.014
retirement_age_1=55
retirement_age_2=60
retirement_age_3=65
avarage_income=(income_1+income_2+income_3)/3

years_of_service_at_retirement_1= retirement_age_1-worker_age+years_of_service
years_of_service_at_retirement_2= retirement_age_2-worker_age+years_of_service
years_of_service_at_retirement_3= retirement_age_3-worker_age+years_of_service

pension_income_1=f"{(avarage_income*rate*years_of_service_at_retirement_1):.2f}"
pension_income_2=f"{(avarage_income*rate*years_of_service_at_retirement_2):.2f}"
pension_income_3=f"{(avarage_income*rate*years_of_service_at_retirement_3):.2f}"

print(f"{'retirement age':<20}{'retirement income':>3}")
print(f"{retirement_age_1:<20}{pension_income_1:>3}")
print(f"{retirement_age_2:<20}{pension_income_2:>3}")
print(f"{retirement_age_3:<20}{pension_income_3:>3}")