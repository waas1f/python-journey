{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c85efb87-86d0-4ec2-990d-d1eaa205e84a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "How many numbers do you want to add? 5\n",
      "Enter your number:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 10\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your number:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 30\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your number:  40\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 70\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your number:  30\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 100\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your number:  50\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total: 150\n",
      "Average: 30.0\n"
     ]
    }
   ],
   "source": [
    "count = int(input(\"How many numbers do you want to add?\"))\n",
    "total = 0\n",
    "for i in range(count):\n",
    "    number=int(input(\"Enter your number: \"))\n",
    "    total= total + number\n",
    "    print(\"Total:\",total)\n",
    "average = total/count\n",
    "print(\"Average:\",average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e24a899c-128e-4300-93bc-4ffe89d4fdf2",
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
