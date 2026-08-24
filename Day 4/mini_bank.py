{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "05c295a9-ff72-4547-bca9-6fe5e4ebb6ec",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your Name: Wasif\n",
      "Enter your Balance: 1000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome! Wasif\n",
      "Current Balance:  1000\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How much do you want to deposit? 500\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Updated Balance: 1500\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to deposit again? (yes/no):  yes\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome! Wasif\n",
      "Current Balance:  1500\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How much do you want to deposit? 200\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Updated Balance: 1700\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Do you want to deposit again? (yes/no):  no\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for using Mini Bank!\n"
     ]
    }
   ],
   "source": [
    "name=input(\"Enter your Name:\")\n",
    "balance=int(input(\"Enter your Balance:\"))\n",
    "def deposit(balance):\n",
    "\n",
    "    choice = \"yes\"\n",
    "\n",
    "    while choice == \"yes\":\n",
    "        print(\"Welcome!\",name)\n",
    "        print(\"Current Balance: \",balance)\n",
    "        deposit_amount = int(input(\"How much do you want to deposit?\"))\n",
    "\n",
    "        balance = balance + deposit_amount\n",
    "\n",
    "        print(\"Updated Balance:\", balance)\n",
    "\n",
    "        choice = input(\"Do you want to deposit again? (yes/no): \").lower()\n",
    "        if choice == \"no\":\n",
    "               print(\"Thank you for using Mini Bank!\")\n",
    "deposit(balance)        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1f0959b-d504-4d6b-877a-55eaff37863e",
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
