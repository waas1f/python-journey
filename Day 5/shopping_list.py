{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6187f0fa-d11c-485e-85ee-e6ce26c76577",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Milk', 'Bread', 'Eggs']\n"
     ]
    }
   ],
   "source": [
    "shopping=[\"Milk\",\"Bread\",\"Eggs\"]\n",
    "print(shopping)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "3334ce53-310e-40c6-8250-1e90b2d70ef4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Milk', 'Bread', 'Eggs', 'Rice']\n"
     ]
    }
   ],
   "source": [
    "shopping.append(\"Rice\")\n",
    "print(shopping)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "fc102e10-5c72-4f19-923a-1cd5deea17fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Perfume', 'Facewash', 'Sunscreen']\n",
      "First item:  Perfume\n",
      "Last item:  Sunscreen\n",
      "['Perfume', 'Facewash', 'Sunscreen', 'Lipbalm', 'Bracelet', 'Necklace']\n",
      "Total items: 6\n"
     ]
    }
   ],
   "source": [
    "shopping=[\"Perfume\",\"Facewash\",\"Sunscreen\"]\n",
    "print(shopping)\n",
    "print(\"First item: \",shopping[0])\n",
    "print(\"Last item: \",shopping[-1])\n",
    "shopping.append(\"Lipbalm\")\n",
    "shopping.append(\"Bracelet\")\n",
    "shopping.append(\"Necklace\")\n",
    "print(shopping)\n",
    "print(\"Total items:\",len(shopping))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8e311c1-eb1f-408a-9d31-07bdf224e856",
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
