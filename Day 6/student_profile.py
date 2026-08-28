{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "101a1a2c-b727-45eb-bc7b-1a847c26af02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Name: Wasif\n",
      "Age: 22\n",
      "University: Beykoz\n",
      "Goal: Entrepreneurship\n"
     ]
    }
   ],
   "source": [
    "student={\n",
    "    \"name\":\"Wasif\",\n",
    "    \"age\": 20\n",
    "}\n",
    "student[\"university\"]=\"Beykoz\"\n",
    "student[\"goal\"]=\"Entrepreneurship\"\n",
    "student.update({\n",
    "    \"age\": 22\n",
    "})\n",
    "print(\"Name:\",student[\"name\"])\n",
    "print(\"Age:\",student[\"age\"])\n",
    "print(\"University:\",student[\"university\"])\n",
    "print(\"Goal:\",student[\"goal\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e877e0a0-b739-42c5-8aac-64a184e62501",
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
