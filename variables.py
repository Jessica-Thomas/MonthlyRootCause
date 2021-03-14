# import csv module, open csv for reading
import csv
with open('ProjectData.csv', newline='') as df:
    reader = csv.reader(df, delimiter=',')
    df.fillna("")

# Isolating columns by filtering for specific text
# Unsure if I actually need all of these, but keeping them around JIC



# Agency Manager
agman1 = df.filter(regex='Agency Manager S1')
agman2 = df.filter(regex='Agency Manager S2')
agman3 = df.filter(regex='Agency Manager S3')
agman4 = df.filter(regex='Agency Manager S4')
# Architecture
arch1 = df.filter(regex='Architecture S1')
arch2 = df.filter(regex='Architecture S2')
arch3 = df.filter(regex='Architecture S3')
arch4 = df.filter(regex='Architecture S4')
# Charge Integrity
charge1 = df.filter(regex='Integrity S1')
charge2 = df.filter(regex='Integrity S2')
charge3 = df.filter(regex='Integrity S3')
charge4 = df.filter(regex='Integrity S4')
# Claims
claims1 = df.filter(regex='Claims S1')
claims2 = df.filter(regex='Claims S2')
claims3 = df.filter(regex='Claims S3')
claims4 = df.filter(regex='Claims S4')
# Contract Management
conman1 = df.filter(regex='Contract Management S1')
conman2 = df.filter(regex='Contract Management S2')
conman3 = df.filter(regex='Contract Management S3')
conman4 = df.filter(regex='Contract Management S4')
# Coverage Detection
covdet1 = df.filter(regex='Coverage Detection S1')
covdet2 = df.filter(regex='Coverage Detection S2')
covdet3 = df.filter(regex='Coverage Detection S3')
covdet4 = df.filter(regex='Coverage Detection S4')
# Denial Management
denman1 = df.filter(regex='Denial Management S1')
denman2 = df.filter(regex='Denial Management S2')
denman3 = df.filter(regex='Denial Management S3')
denman4 = df.filter(regex='Denial Management S4')
# Eligibility
elig1 = df.filter(regex='Eligibility S1')
elig2 = df.filter(regex='Eligibility S2')
elig3 = df.filter(regex='Eligibility S3')
elig4 = df.filter(regex='Eligibility S4')
# Estimation
est1 = df.filter(regex='Estimation S1')
est2 = df.filter(regex='Estimation S2')
est3 = df.filter(regex='Estimation S3')
est4 = df.filter(regex='Estimation S4')
# Infrastructure
infra1 = df.filter(regex='Infrastructure S1')
infra2 = df.filter(regex='Infrastructure S2')
infra3 = df.filter(regex='Infrastructure S3')
infra4 = df.filter(regex='Infrastructure S4')
# Internal
internal1 = df.filter(regex='Internal S1')
internal2 = df.filter(regex='Internal S2')
internal3 = df.filter(regex='Internal S3')
internal4 = df.filter(regex='Internal S4')
# Patient Payments
paypay1 = df.filter(regex='Payments S1')
paypay2 = df.filter(regex='Payments S2')
paypay3 = df.filter(regex='Payments S3')
paypay4 = df.filter(regex='Payments S4')
# Remits
remits1 = df.filter(regex='Remits S1')
remits2 = df.filter(regex='Remits S2')
remits3 = df.filter(regex='Remits S3')
remits4 = df.filter(regex='Remits S4')
# All
all1 = df.filter(regex='All S1')
all2 = df.filter(regex='All S2')
all3 = df.filter(regex='All S3')
all4 = df.filter(regex='All S4')



