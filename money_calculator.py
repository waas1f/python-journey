{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1b57d21d-5609-4347-bfa7-1aa8a0bfeac9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Whats your monthly income? 500\n",
      "Whats your monthly expenses? 300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Monthly Savings: 200\n",
      "Yearly Income: 6000\n",
      "Yearly Expenses: 3600\n",
      "Yearly Savings: 2400\n"
     ]
    }
   ],
   "source": [
    "monthly_income = int(input(\"Whats your monthly income?\"))\n",
    "monthly_expenses = int(input(\"Whats your monthly expenses?\"))\n",
    "monthly_savings = (monthly_income - monthly_expenses)\n",
    "yearly_income = (monthly_income *12)\n",
    "yearly_expenses = (monthly_expenses *12)\n",
    "yearly_savings = (monthly_savings *12)\n",
    "print(\"Monthly Savings:\",monthly_savings)\n",
    "print(\"Yearly Income:\",yearly_income)\n",
    "print(\"Yearly Expenses:\",yearly_expenses)\n",
    "print(\"Yearly Savings:\",yearly_savings)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3e82bcd-0d60-459e-93db-f84e16de0bce",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
