#Project Details

The project analyzes salaries data in the STEM (science, technology, ingineering and mathematics) industry, as well as the factors that might influence the salary level.

#Questions to Answer

1. Which positions are in demand in the industry?
2. Who are the top employers in the industry?
3. Where are the positions located geograficaly?
4. Does demographics play a factor in the industry?
5. Do factors like geo, demo, company, years of experience, position level influence salary?

#Data

Dataset includes around 23.000 entries from 2021. The majority of positins are located in the USA. The dataset was cleaned by using feature selection and dimentionality reduction. The missing values were replaces in different ways depending on the feature, e.g. creating a new category, knn imputer.

#LM Models

Since the target variable is numerical, 3 supervised regression models were trained: Linear Regreddion, KNN Regressor and Decision Tree Regressor. 

#Results

The model with the best results was KNN Regressor with r2 of 0.58. This means that the model can explain around 58% of variance in data.
This result is moderate.

#Further applications