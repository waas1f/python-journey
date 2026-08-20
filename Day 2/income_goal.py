{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "869b1e62-c4b7-4b22-a6f4-82c366f428b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Whats your monthly income?:  650\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You exceeded your goal by $ 150\n"
     ]
    }
   ],
   "source": [
    "goal = 500\n",
    "income = int(input(\"Whats your monthly income?: \"))\n",
    "    \n",
    "if income==goal:\n",
    "             print(\"Goal Achieved\")\n",
    "elif income>goal:\n",
    "    print(\"You exceeded your goal by $\",income-goal)\n",
    "elif income<goal:\n",
    "    print(\"Keep working you are short by $\",goal-income)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "456da52a-29dc-4646-8412-c7fc0f767358",
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
