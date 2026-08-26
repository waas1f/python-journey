{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "da76a91b-521f-4242-af31-7aa7bd1ade69",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  30\n",
      "Enter second number:  13\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Addition: 43\n",
      "Subtraction:  17\n",
      "Division:  2.3076923076923075\n",
      "Multiplication:  390\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter first number: \"))\n",
    "b=int(input(\"Enter second number: \"))\n",
    "def add(a,b):\n",
    "    return a + b\n",
    "result=add(a,b)\n",
    "print(\"Addition:\",result)\n",
    "def subtract(a,b):\n",
    "    return a-b\n",
    "result=subtract(a,b)\n",
    "print(\"Subtraction: \",result)\n",
    "def divide(a,b):\n",
    "    return a/b\n",
    "result=divide(a,b)\n",
    "print(\"Division: \",result)\n",
    "def multiply(a,b):\n",
    "    return a * b\n",
    "result=multiply(a,b)\n",
    "print(\"Multiplication: \",result)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5cf26b6e-16d7-4bdd-8013-a9b3151592f7",
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
