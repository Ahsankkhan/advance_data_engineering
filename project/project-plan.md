#Project Plan

##Title

Interlinked Dynamics: Exploring the Correlations between Chronic Disease Indicators and Specific Death Rates

##Main Questions

1. Are there correlations between chronic disease indicators (e.g., diabetes prevalence) and specific death rates (e.g., due to heart disease)?

2. What were the leading causes of death each year between 2020 and 2023?

##Description

This data science project aims to analyze the relationships between chronic disease indicators[^r2] and mortality rates in the United States over the period from 2020 to 2023[^r1]. By exploring datasets on chronic disease prevalence and causes of death, the project seeks to identify potential correlations that could inform public health initiatives and resource allocation.

The analysis will focus on chronic diseases such as diabetes, heart disease, and cancer, utilizing publicly available datasets to extract and analyze relevant data. The goal is to assess how the prevalence of chronic diseases may influence death rates from various causes and to identify trends in leading causes of death over the specified years. This project will leverage statistical models and data visualization techniques to derive insights that can contribute to improved health outcomes and policy decisions.

##Datasources

###Datasource 1: Monthly Provisional Counts of Deaths by Select Causes (2020-2023)
*Metadata URL: https://catalog.data.gov/dataset/monthly-counts-of-deaths-by-select-causes-2020-2021-2785a
*Data URL: https://data.cdc.gov/api/views/9dzk-mvmi/rows.csv?accessType=DOWNLOAD
*Data Type: CSV

This dataset contains provisional counts of deaths by month for various causes, including chronic diseases and COVID-19, from 2020 to 2023. It enables analysis of trends in mortality rates across different demographics and causes.

###Datasource 2: U.S. Chronic Disease Indicators (CDI)
*Description: https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi
*Data URL: https://data.cdc.gov/api/views/g4ie-h725/rows.csv?accessType=DOWNLOAD
*Data Type: CSV

This dataset provides a comprehensive set of chronic disease indicators, allowing for state-specific analyses of diseases such as diabetes, heart disease, and cancer. It includes demographic stratifications and historical data, facilitating comparative analyses across different regions and time periods.

##Work Packages
This project is structured into six work packages, represented as [milestones in the GitHub repository](https://github.com/Ahsankkhan/advance_data_engineering/milestones?with_issues=no).

1. **Project Definition and Data Source Selection** [[WP1](https://github.com/Ahsankkhan/advance_data_engineering/milestone/1)]
    1. Define the research topic on a given theme.
    2. Define the research question on a selected topic.
    3. Locate potential data sources.
    4. Evaluate the identified data sources.
2. **Data Acquisition and Pipeline** [[WP2](https://github.com/Ahsankkhan/advance_data_engineering/milestone/2)]
    1. Determine the best data storage format.
    3. Data Pipeline.
3. **Data Exploration, Analytics and Report** [[WP3](https://github.com/Ahsankkhan/advance_data_engineering/milestone/3)]
    1. Conduct exploratory data analysis and preliminary visualization.
    2. Create DataLoader, Pipeline, Visualizations, Models, etc.
    3. Address all the research questions.
    4. Draw conclusions form the analysis. 
4. **Automated Testing** [[WP4](https://github.com/Ahsankkhan/advance_data_engineering/milestone/4)]
    1. Create Tests.
5. **Continuous integration** [[WP5](https://github.com/Ahsankkhan/advance_data_engineering/milestone/5)]
    1. Develop CI.
    2. Develop CI for Pre-Commit.
6. **Final Report** [[WP6](https://github.com/Ahsankkhan/advance_data_engineering/milestone/6)]
    1. Develop visual representations. 
    2. Enhance the repository's presentation. 
    3. Prepare the final presentation.


Work packages must be completed sequentially as each one depends on the completion of all preceding ones.

## References and footnotes

[^r1]:https://catalog.data.gov/dataset/monthly-counts-of-deaths-by-select-causes-2020-2021-2785a

[^r2]:https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi