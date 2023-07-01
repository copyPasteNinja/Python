#!/bin/env python3

income = 250_000

low_tax_rate = 0.05
rip_off_land_rate = 0.43

diff = (income * rip_off_land_rate) - (income * low_tax_rate)

print(f"Your income is {income} and you would pay {income * low_tax_rate} income tax in Lowtaxland or {income * rip_off_land_rate} income tax in Ripoffland. You would save {diff} by paying taxes in Lowtaxland!")

