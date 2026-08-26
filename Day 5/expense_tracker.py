{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8efc339f-aae9-46a8-bb07-29fbcbe33547",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many expenses do you have? 5\n",
      "Expense 1: 123\n",
      "Expense 2: 34\n",
      "Expense 3: 567\n",
      "Expense 4: 900\n",
      "Expense 5: 45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Your Expenses:\n",
      "Expense 1 : 123\n",
      "Expense 2 : 34\n",
      "Expense 3 : 567\n",
      "Expense 4 : 900\n",
      "Expense 5 : 45\n",
      "Total Expenses: 799\n",
      "Highest Expense: 900\n",
      "Lowest Expense: 34\n",
      "Average Expense: 333.8\n"
     ]
    }
   ],
   "source": [
    "number_of_expenses=int(input(\"How many expenses do you have?\"))\n",
    "expense_list=[]\n",
    "for i in range(number_of_expenses):\n",
    "    expense=int(input(f\"Expense {i+1}:\"))\n",
    "    expense_list.append(expense)\n",
    "print(\"\\nYour Expenses:\")\n",
    "for i in range(len(expense_list)):\n",
    "    print(\"Expense\",i+1,\":\",expense_list[i])\n",
    "def calculate_total(expense_list):\n",
    "    total = sum(expense_list)   \n",
    "    total = calculate_total(expense_list)   \n",
    "    return total\n",
    "print(\"Total Expenses:\",total)\n",
    "print(\"Highest Expense:\",max(expense_list))\n",
    "print(\"Lowest Expense:\",min(expense_list))\n",
    "average=sum(expense_list)/len(expense_list)\n",
    "print(\"Average Expense:\",average)\n",
    "    \n",
    "    \n",
    "\n",
    "    \n",
    "                  \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f1367024-5d20-4653-88ae-d198c39d9d56",
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
