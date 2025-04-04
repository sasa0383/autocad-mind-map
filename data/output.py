data = {
    'Advanced Statistics': {
        '1. Introduction to Statistics': {
            '1.1 Probability Theory': {
                '1.1.1 Random Experiment': {
                    'Definition': {
                        'Definition': {
                            'A random experiment is any process or action that can produce a set of outcomes but whose specific result cannot be predicted with certainty in advance. Unlike deterministic experiments, random experiments involve uncertainty.': {
                            },
                        },
                    },
                    'Key Characteristics': {
                        'Unpredictable Outcome': {
                            'The result of the experiment cannot be determined beforehand.': {
                            },
                        },
                        'Repeatability': {
                            'The experiment can be repeated under the same conditions to observe outcomes.': {
                            },
                        },
                        'Set of Possible Outcomes': {
                            'The total collection of all possible outcomes is known as the sample space.': {
                            },
                        },
                    },
                    'Examples': {
                        'Coin Toss': {
                            "Description: Tossing a coin produces either 'Heads' or 'Tails'.": {
                            },
                            'Sample Space: S = {Heads, Tails}.': {
                            },
                            'Outcome: The specific result of a single toss (e.g., Heads).': {
                            },
                        },
                        'Rolling a Die': {
                            'Description: Rolling a standard six-sided die produces a number between 1 and 6.': {
                            },
                            'Sample Space: S = {1, 2, 3, 4, 5, 6}.': {
                            },
                            'Outcome: The number rolled, e.g., 4.': {
                            },
                        },
                        'Drawing a Card': {
                            'Description: Drawing one card from a standard 52-card deck.': {
                            },
                            'Sample Space: All possible cards in a 52-card deck.': {
                            },
                            'Outcome: A single card drawn, e.g., 7 of Diamonds.': {
                            },
                        },
                        'Lifetime of a Lightbulb': {
                            'Description: Testing the lifespan of a lightbulb until it fails.': {
                            },
                            'Sample Space: A set of possible lifetimes, e.g., [0, âˆž).': {
                            },
                            'Outcome: The actual lifetime of a specific bulb, e.g., 500 hours.': {
                            },
                        },
                    },
                },
                '1.1.2 Sample Space, Event, Outcome': {
                    'Definition': {
                        'Sample Space (S)': {
                            'The set of all possible outcomes of a random experiment. Example: For a single coin toss, the sample space is S=H,T.': {
                            },
                        },
                        'Event (E)': {
                            'A subset of the sample space representing specific outcomes. Example: Rolling an even number E=2,4,6.': {
                            },
                        },
                        'Outcome (Ï‰)': {
                            'A single result of a random experiment. Example: Rolling a die and getting 5 Ï‰=5.': {
                            },
                        },
                    },
                    'Examples': {
                        'Coin Toss': {
                            'Sample Space S={H,T}, Event E=H, Outcome Ï‰=T.': {
                            },
                        },
                        'Rolling a Die': {
                            'Sample Space S={1,2,3,4,5,6}, Event E=2,4,6, Outcome Ï‰=3.': {
                            },
                        },
                        'Drawing a Card': {
                            'Sample Space: All cards in a deck, Event: Drawing a red card, Outcome: Drawing King of Hearts.': {
                            },
                        },
                    },
                    'Types of Sample Spaces': {
                        'Finite Sample Space': {
                            'Contains a finite number of outcomes. Example: Rolling a die.': {
                            },
                        },
                        'Infinite Sample Space': {
                            'Contains an infinite number of outcomes. Example: Lifetime of a lightbulb.': {
                            },
                        },
                        'Discrete Sample Space': {
                            'Outcomes can be listed individually. Example: Flipping a coin.': {
                            },
                        },
                        'Continuous Sample Space': {
                            'Outcomes fall within a range. Example: Measuring height.': {
                            },
                        },
                    },
                    'Properties of Events': {
                        'Union of Events (A âˆª B)': {
                            'Includes all outcomes in either A, B, or both.': {
                            },
                        },
                        'Intersection of Events (A âˆ© B)': {
                            'Includes only outcomes in both A and B.': {
                            },
                        },
                        'Complement of an Event (Aá¶œ)': {
                            'Includes all outcomes in S not in A.': {
                            },
                        },
                        'Mutually Exclusive Events': {
                            'Events that cannot occur simultaneously.': {
                            },
                        },
                    },
                    'Real-World Applications': {
                        'Quality Control': {
                            'Sample Space: S={Pass,Fail}, Event: Passing at least 90%.': {
                            },
                        },
                        'Finance': {
                            'Sample Space: S={Increase,Decrease,NoChange}, Event: Stock price increases.': {
                            },
                        },
                        'Sports': {
                            'Sample Space: S={Win,Lose,Draw}, Event: Winning the match.': {
                            },
                        },
                    },
                },
                '1.1.3 Random Variable': {
                    'Definition': {
                        'Definition': {
                            'A random variable assigns a numerical value to each outcome of a random experiment.': {
                            },
                        },
                        'Formal Definition': {
                            'Maps outcomes in a sample space S to real numbers (R).': {
                            },
                        },
                    },
                    'Types of Random Variables': {
                        'Discrete Random Variable': {
                            'Takes a finite or countably infinite number of distinct values.': {
                            },
                        },
                        'Continuous Random Variable': {
                            'Takes values from an uncountable range, usually an interval of real numbers.': {
                            },
                        },
                    },
                    'Probability Distribution': {
                        'PMF (Discrete)': {
                            'Assigns probabilities to specific values of the random variable.': {
                            },
                        },
                        'PDF (Continuous)': {
                            'Represents the relative likelihood of the random variable taking a value in an interval.': {
                            },
                        },
                    },
                    'Examples': {
                        'Coin Toss': {
                            'Number of heads in 3 tosses, PMF: P(X=0)=1/8, P(X=1)=3/8, etc.': {
                            },
                        },
                        'Rolling a Die': {
                            'The value shown on the die, PMF: P(X=x)=1/6 for x=1,2,3,4,5,6.': {
                            },
                        },
                        'Height of a Person': {
                            'Height of a randomly selected person, PDF describes the probability density.': {
                            },
                        },
                        'Time to Complete a Task': {
                            'Time taken to finish a task, PDF gives the probability density for specific times.': {
                            },
                        },
                    },
                    'Expectation and Variance': {
                        'Expectation (Mean)': {
                            'Average value of a random variable over many trials.': {
                            },
                        },
                        'Variance': {
                            "Measures the spread of a random variable's values.": {
                            },
                        },
                    },
                    'Real-World Applications': {
                        'Finance': {
                            'Random Variable: Daily return on a stock, Use: Estimate risk and expected returns.': {
                            },
                        },
                        'Manufacturing': {
                            'Random Variable: Number of defective products in a batch, Use: Improve quality control processes.': {
                            },
                        },
                        'Healthcare': {
                            'Random Variable: Time until a patient recovers from treatment, Use: Predict treatment outcomes.': {
                            },
                        },
                        'Weather Forecasting': {
                            'Random Variable: Amount of rainfall in a day, Use: Estimate probabilities of extreme weather events.': {
                            },
                        },
                    },
                },
                '1.1.5 Conditional Probability': {
                    'Definition': {
                        'Definition': {
                            'Conditional probability measures the probability of an event A occurring given that another event B has already occurred.': {
                            },
                        },
                        'Mathematical Representation': {
                            'P(A|B) = P(Aâˆ©B) / P(B), where P(B) > 0.': {
                            },
                        },
                    },
                    'Explanation': {
                        'Intuition': {
                            "Conditional probability 'zooms in' on a subset of the sample space where B is true.": {
                            },
                        },
                    },
                    'Examples': {
                        'Rolling a Die': {
                            'P(A|B): Probability of rolling an even number given the number is greater than 3.': {
                            },
                        },
                        'Card Drawing': {
                            'P(A|B): Probability of drawing a King given the card is red.': {
                            },
                        },
                    },
                    'Law of Total Probability': {
                        'Definition': {
                            'P(A) = âˆ‘ P(A|B_i) â‹… P(B_i), where B_i are mutually exclusive events.': {
                            },
                        },
                    },
                    'Real-World Applications': {
                        'Disease Testing': {
                            'P(A|B): Likelihood of having the disease given a positive test result.': {
                            },
                        },
                        'Weather Forecasting': {
                            'P(A|B): Probability of rain given clouds today.': {
                            },
                        },
                        'Manufacturing': {
                            'P(A|B): Likelihood of defects given failures in quality control.': {
                            },
                        },
                    },
                    'Key Properties': {
                        'Multiplicative Rule': {
                            'P(Aâˆ©B) = P(A|B) â‹… P(B).': {
                            },
                        },
                        "Bayes' Theorem": {
                            'P(B|A) = [P(A|B) â‹… P(B)] / P(A).': {
                            },
                        },
                    },
                },
                '1.1.6 Real-World Example': {
                    'Disease Testing': {
                        'Scenario': {
                            'A medical test is used to detect a rare disease with known probabilities.': {
                            },
                        },
                        'Objective': {
                            'What is the probability that a person who tests positive actually has the disease?': {
                            },
                        },
                        "Solution Using Bayes' Theorem": {
                            'P(Disease|Positive) = [P(Positive|Disease) â‹… P(Disease)] / P(Positive).': {
                            },
                        },
                        'Key Calculation': {
                            'P(Positive) = P(Positive|Disease) â‹… P(Disease) + P(Positive|NoDisease) â‹… P(NoDisease).': {
                            },
                        },
                        'Calculation Result': {
                            'P(Disease|Positive) â‰ˆ 0.0472 or 4.72%.': {
                            },
                        },
                        'Interpretation': {
                            'Even with an accurate test, low disease prevalence leads to many false positives.': {
                            },
                        },
                        'Key Concepts': {
                            'Demonstrates conditional probability, false positives, and Bayesian reasoning.': {
                            },
                        },
                    },
                    'Real-World Applications': {
                        'Finance': {
                            'Determining the probability of market crashes given specific economic indicators.': {
                            },
                        },
                        'Weather Forecasting': {
                            'Estimating the likelihood of rain given cloud cover and humidity.': {
                            },
                        },
                        'Spam Detection': {
                            'Identifying whether an email is spam based on certain keywords.': {
                            },
                        },
                    },
                },
            },
        },
        'Unit 2: Descriptive Statistics': {
            '2.1 Mean, Median, Mode, and Quantiles': {
                'Definition': {
                    'Mean': {
                        'The arithmetic average of all data points.': {
                        },
                    },
                    'Median': {
                        'The middle value in a sorted data set.': {
                        },
                    },
                    'Mode': {
                        'The most frequently occurring value(s) in the data.': {
                        },
                    },
                    'Quantiles': {
                        'Values that divide the data set into equal parts, e.g., quartiles (4 parts).': {
                        },
                    },
                },
                'Examples': {
                    'Dataset': {
                        '[4, 6, 7, 3, 2, 9]': {
                        },
                    },
                    'Mean': {
                        5.167: {
                        },
                    },
                    'Median': {
                        5: {
                        },
                    },
                    'Mode': {
                        'No repeating values (No mode).': {
                        },
                    },
                },
                'Applications': {
                    'Mean': {
                        'Useful for summarizing central tendencies.': {
                        },
                    },
                    'Median': {
                        'Robust to outliers.': {
                        },
                    },
                    'Mode': {
                        'Identifies the most common occurrence.': {
                        },
                    },
                },
            },
            '2.2 Variance, Skewness, and Kurtosis': {
                'Definition': {
                    'Variance': {
                        'Measures the spread of data points.': {
                        },
                    },
                    'Skewness': {
                        'Measures the asymmetry of the data distribution.': {
                        },
                    },
                    'Kurtosis': {
                        "Describes the 'tailedness' of the distribution.": {
                        },
                    },
                },
                'Examples': {
                    'Dataset': {
                        '[1, 2, 2, 3, 4, 7, 9]': {
                        },
                    },
                    'Variance': {
                        8.5: {
                        },
                    },
                    'Skewness': {
                        'Positive': {
                        },
                    },
                    'Kurtosis': {
                        'Moderate tails': {
                        },
                    },
                },
                'Applications': {
                    'Variance': {
                        'Quantifies variability.': {
                        },
                    },
                    'Skewness': {
                        'Used for understanding data symmetry.': {
                        },
                    },
                    'Kurtosis': {
                        'Analyzes tail properties in risk analysis.': {
                        },
                    },
                },
            },
            '2.3 Real-World Applications of Descriptive Statistics': {
                'Summarizing Large Datasets': {
                    'Example': {
                        'Analyzing sensor data to identify trends.': {
                        },
                    },
                    'Use': {
                        'Mean and variance for central tendency and variability.': {
                        },
                    },
                },
                'Quality Control': {
                    'Example': {
                        'Checking product weights in manufacturing.': {
                        },
                    },
                    'Use': {
                        'Variance and skewness for deviations from the standard.': {
                        },
                    },
                },
                'Economic Indicators': {
                    'Example': {
                        'Average income, wealth distribution.': {
                        },
                    },
                    'Use': {
                        'Median for robust central tendency.': {
                        },
                    },
                },
            },
        },
        'Unit 3: Probability Distributions': {
            '3.1 Binomial and Negative Binomial Distribution': {
                'Binomial Distribution': {
                    'Definition': {
                        'Models the number of successes in n independent Bernoulli trials, each with success probability p.': {
                        },
                    },
                    'PMF': {
                        'P(X=k) = (n choose k) * p^k * (1-p)^(n-k), k=0,1,...,n': {
                        },
                    },
                    'Example': {
                        'Tossing a coin 10 times with p=0.5 to find the probability of exactly 4 heads.': {
                        },
                    },
                },
                'Negative Binomial Distribution': {
                    'Definition': {
                        'Models the number of trials needed to achieve r successes in independent Bernoulli trials.': {
                        },
                    },
                    'PMF': {
                        'P(X=k) = (k+r-1 choose r-1) * p^r * (1-p)^k, k=0,1,2,...': {
                        },
                    },
                    'Example': {
                        'Counting the number of coin tosses required to get 3 heads.': {
                        },
                    },
                },
            },
            '3.2 Gaussian (Normal) Distribution': {
                'Definition': {
                    'Definition': {
                        'Represents continuous data with a symmetric, bell-shaped curve centered around the mean Î¼.': {
                        },
                    },
                    'PDF': {
                        'f(x) = (1 / sqrt(2Ï€Ïƒ^2)) * e^(-(x-Î¼)^2 / (2Ïƒ^2))': {
                        },
                    },
                },
                'Example': {
                    'Example': {
                        'Heights of adults with mean height 170 cm and standard deviation 10 cm.': {
                        },
                    },
                },
            },
            '3.3 Poisson, Gamma-Poisson, and Exponential Distributions': {
                'Poisson Distribution': {
                    'Definition': {
                        'Models the number of events occurring in a fixed interval with mean rate Î».': {
                        },
                    },
                    'PMF': {
                        'P(X=k) = (Î»^k * e^(-Î»)) / k!, k=0,1,2,...': {
                        },
                    },
                    'Example': {
                        'Number of cars passing through a toll booth per minute.': {
                        },
                    },
                },
                'Exponential Distribution': {
                    'Definition': {
                        'Models the time between events in a Poisson process.': {
                        },
                    },
                    'PDF': {
                        'f(x) = Î» * e^(-Î»x), x â‰¥ 0': {
                        },
                    },
                    'Example': {
                        'Time between arrivals of customers at a service desk.': {
                        },
                    },
                },
            },
            '3.4 Weibull Distribution': {
                'Definition': {
                    'Definition': {
                        'Models the time until failure in reliability analysis.': {
                        },
                    },
                    'PDF': {
                        'f(x) = (k/Î») * (x/Î»)^(k-1) * e^(-(x/Î»)^k), x â‰¥ 0': {
                        },
                    },
                },
                'Example': {
                    'Example': {
                        'Modeling the lifespan of electronic components.': {
                        },
                    },
                },
            },
            '3.5 Transformed Random Variables': {
                'Definition': {
                    'Definition': {
                        'When random variables undergo transformations, their distributions change accordingly.': {
                        },
                    },
                },
                'Example': {
                    'Example': {
                        'If X~N(Î¼,Ïƒ^2), then Y=aX+b follows a Normal distribution with mean aÎ¼+b and variance a^2Ïƒ^2.': {
                        },
                    },
                },
            },
        },
        'Unit 4: Bayesian Statistics': {
            "4.1 Bayes' Rule": {
                'Definition': {
                    'Definition': {
                        'A formula that updates the probability of a hypothesis based on new evidence.': {
                        },
                    },
                },
                'Mathematical Representation': {
                    'Formula': {
                        'P(H|E) = [P(E|H) * P(H)] / P(E)': {
                        },
                    },
                    'Explanation': {
                        'Posterior = Prior * Likelihood / Marginal Probability.': {
                        },
                    },
                },
                'Example': {
                    'Medical Diagnosis': {
                        "Using Bayes' Rule to determine the probability a patient has a disease given a positive test result.": {
                        },
                    },
                },
            },
            "4.2 Estimating the Prior, Benford's Law, and Jeffrey's Rule": {
                'Estimating the Prior': {
                    'Definition': {
                        'Reflects initial beliefs before observing data.': {
                        },
                    },
                    'Example': {
                        'In voting, prior probability may be based on previous election results.': {
                        },
                    },
                },
                "Benford's Law": {
                    'Definition': {
                        'In many datasets, smaller digits appear as the first digit more frequently.': {
                        },
                    },
                },
                "Jeffrey's Rule": {
                    'Definition': {
                        'Assigns non-informative priors when no prior information is available.': {
                        },
                    },
                },
            },
            '4.3 Conjugate Priors': {
                'Definition': {
                    'Definition': {
                        'A prior distribution that results in a posterior of the same family when combined with the likelihood.': {
                        },
                    },
                },
                'Example': {
                    'Coin Toss': {
                        'Using a beta prior for the probability of heads results in a beta posterior after observing outcomes.': {
                        },
                    },
                },
            },
            '4.4 Bayesian and Frequentist Approach': {
                'Bayesian Approach': {
                    'Definition': {
                        'Incorporates prior knowledge and treats parameters as random variables.': {
                        },
                    },
                    'Example': {
                        'Using prior beliefs about election outcomes to update predictions after polling data.': {
                        },
                    },
                },
                'Frequentist Approach': {
                    'Definition': {
                        'Does not use prior probabilities and treats parameters as fixed but unknown.': {
                        },
                    },
                    'Example': {
                        'Estimating the probability of heads by repeatedly tossing a coin.': {
                        },
                    },
                },
                'Comparison': {
                    'Comparison': {
                        'Bayesian methods are flexible but may introduce subjectivity. Frequentist methods avoid subjectivity but require large datasets.': {
                        },
                    },
                },
            },
        },
        'Unit 5: Data Visualization': {
            '5.1 General Principles': {
                'Overview': {
                    'Overview': {
                        'Data visualization is a critical tool for understanding and communicating data insights.': {
                        },
                    },
                },
                'Key Principles': {
                    'Chart Selection': {
                        'Select the appropriate chart type to represent data effectively.': {
                        },
                    },
                    'Clarity': {
                        'Design visualizations with clarity to avoid cognitive biases.': {
                        },
                    },
                    'Consistency': {
                        'Use consistent styles, labels, and legends for better understanding.': {
                        },
                    },
                },
                'Example': {
                    'Sensor Data': {
                        'Scatter plot shows each data point; line chart implies continuity and trends.': {
                        },
                    },
                },
            },
            '5.2 One- and Two-Dimensional Histograms': {
                'Histograms': {
                    'Definition': {
                        'Represent the frequency of data points within defined intervals (bins).': {
                        },
                    },
                    'One-Dimensional': {
                        'Histograms show the distribution of a single variable.': {
                        },
                    },
                    'Two-Dimensional': {
                        'Heatmaps visualize relationships between two variables.': {
                        },
                    },
                },
                'Examples': {
                    'One-Dimensional': {
                        "Histogram showing frequency of students' test scores.": {
                        },
                    },
                    'Two-Dimensional': {
                        'Heatmap of temperature versus humidity over time.': {
                        },
                    },
                },
            },
            '5.3 Box and Violin Plots': {
                'Box Plots': {
                    'Definition': {
                        'Summarize data distribution with median, quartiles, and outliers.': {
                        },
                    },
                },
                'Violin Plots': {
                    'Definition': {
                        'Combine box plots and kernel density estimates for richer visualization.': {
                        },
                    },
                },
                'Examples': {
                    'Box Plot': {
                        'Comparing exam scores across different classes.': {
                        },
                    },
                    'Violin Plot': {
                        'Income distribution by region.': {
                        },
                    },
                },
            },
            '5.4 Scatter and Profile Plots': {
                'Scatter Plots': {
                    'Definition': {
                        'Visualize the relationship between two continuous variables.': {
                        },
                    },
                },
                'Profile Plots': {
                    'Definition': {
                        'Aggregate data points to represent trends in large datasets.': {
                        },
                    },
                },
                'Examples': {
                    'Scatter Plot': {
                        'Age versus income to study correlation.': {
                        },
                    },
                    'Profile Plot': {
                        'Average daily sales over a year.': {
                        },
                    },
                },
            },
            '5.5 Bar Plots': {
                'Bar Charts': {
                    'Definition': {
                        'Compare categorical data or discrete variables.': {
                        },
                    },
                    'Types': {
                        'Grouped, stacked, or horizontal bars.': {
                        },
                    },
                },
                'Examples': {
                    'Bar Chart': {
                        'Product sales by category.': {
                        },
                    },
                    'Stacked Bar Chart': {
                        'Monthly expenses by category.': {
                        },
                    },
                },
            },
        },
        'Unit 6: Parameter Estimation': {
            '6.1 Maximum Likelihood Estimation (MLE)': {
                'Definition': {
                    'Definition': {
                        'A method to estimate parameters by maximizing the likelihood function of the observed data.': {
                        },
                    },
                },
                'Steps': {
                    'Step 1': {
                        'Define the likelihood function L(Î¸) = P(X|Î¸).': {
                        },
                    },
                    'Step 2': {
                        'Take the natural logarithm to simplify: â„“(Î¸) = ln(L(Î¸)).': {
                        },
                    },
                    'Step 3': {
                        'Maximize â„“(Î¸) to find the parameter estimates.': {
                        },
                    },
                },
                'Example': {
                    'Normal Distribution': {
                        'Estimate Î¼ and Ïƒ^2 for a sample from N(Î¼, Ïƒ^2).': {
                        },
                    },
                },
            },
            '6.2 Ordinary Least Squares (OLS)': {
                'Definition': {
                    'Definition': {
                        'A method to estimate parameters in a linear regression model by minimizing the sum of squared residuals.': {
                        },
                    },
                },
                'Cost Function': {
                    'Formula': {
                        'J(Î²) = Î£(y_i - Î²_0 - Î²_1 * x_i)^2.': {
                        },
                    },
                },
                'Example': {
                    'Linear Regression': {
                        'Fit a line to dataset X=[1,2,3], Y=[2,4,6].': {
                        },
                    },
                },
            },
            '6.3 Expectation Maximization (EM)': {
                'Definition': {
                    'Definition': {
                        'An iterative method for finding MLE when the data is incomplete or has hidden variables.': {
                        },
                    },
                },
                'Steps': {
                    'Step 1 (E-step)': {
                        'Compute the expected value of the log-likelihood function with current parameter estimates.': {
                        },
                    },
                    'Step 2 (M-step)': {
                        'Maximize this expected log-likelihood to update the parameters.': {
                        },
                    },
                },
                'Example': {
                    'Gaussian Mixture Model': {
                        'Estimate mean, variance, and probabilities for two Gaussian distributions.': {
                        },
                    },
                },
            },
            '6.4 Lasso and Ridge Regularization': {
                'Lasso Regularization': {
                    'Definition': {
                        'Adds an L1 penalty to the cost function, encouraging sparsity in coefficients.': {
                        },
                    },
                },
                'Ridge Regularization': {
                    'Definition': {
                        'Adds an L2 penalty to the cost function, shrinking coefficients towards zero.': {
                        },
                    },
                },
                'Example': {
                    'House Price Prediction': {
                        'Lasso selects important features; Ridge reduces multicollinearity.': {
                        },
                    },
                },
            },
            '6.5 Propagation of Uncertainties': {
                'Definition': {
                    'Definition': {
                        'Describes how uncertainties in measurements propagate to computed quantities.': {
                        },
                    },
                },
                'Formula': {
                    'Formula': {
                        'Ïƒ_y^2 = (âˆ‚y/âˆ‚x1)^2 * Ïƒ_x1^2 + (âˆ‚y/âˆ‚x2)^2 * Ïƒ_x2^2.': {
                        },
                    },
                },
                'Example': {
                    'Measurement Addition': {
                        'For z = x + y, Ïƒ_z = âˆš(Ïƒ_x^2 + Ïƒ_y^2).': {
                        },
                    },
                },
            },
        },
        'Unit 7: Hypothesis Testing': {
            '7.1 Type I and Type II Errors': {
                'Definition': {
                    'Type I Error': {
                        'Rejecting the null hypothesis (H0) when it is true.': {
                        },
                    },
                    'Type II Error': {
                        'Failing to reject the null hypothesis (H0) when it is false.': {
                        },
                    },
                },
                'Key Points': {
                    'Significance Level': {
                        'Probability of making a Type I Error.': {
                        },
                    },
                    'Power of the Test': {
                        'Probability of correctly rejecting the null hypothesis.': {
                        },
                    },
                },
                'Graphical Representation': {
                    'Overlap': {
                        'Distribution curves illustrate regions for rejecting H0 and H1, showing error overlap.': {
                        },
                    },
                },
            },
            '7.2 p-Values': {
                'Definition': {
                    'Definition': {
                        'The p-value measures the probability of obtaining a test statistic as extreme as observed, assuming H0 is true.': {
                        },
                    },
                },
                'Interpretation': {
                    'Small p-Value': {
                        'p<Î± indicates evidence against H0; reject H0.': {
                        },
                    },
                    'Large p-Value': {
                        'pâ‰¥Î± indicates insufficient evidence to reject H0.': {
                        },
                    },
                },
                'Example': {
                    'Coin Fairness': {
                        'Testing if a coin is fair: p=0.03, Î±=0.05; reject H0, indicating bias.': {
                        },
                    },
                },
            },
            '7.3 Multiple Hypothesis Testing': {
                'Definition': {
                    'Definition': {
                        'Testing multiple hypotheses increases the probability of making at least one Type I Error.': {
                        },
                    },
                },
                'Solutions': {
                    'Bonferroni Correction': {
                        "Adjust Î± for the number of tests: Î±'=Î±/n.": {
                        },
                    },
                    'False Discovery Rate': {
                        'Control the proportion of false positives among rejected hypotheses.': {
                        },
                    },
                },
                'Example': {
                    'Gene Testing': {
                        'Testing expressions in 1000 genes using FDR to ensure no more than 5% false discoveries.': {
                        },
                    },
                },
            },
            'Key Steps in Hypothesis Testing': {
                'Step 1': {
                    'Formulate Hypotheses': {
                        'H0: Default assumption; H1: Opposite of H0.': {
                        },
                    },
                },
                'Step 2': {
                    'Choose Significance Level': {
                        'Common values: 0.01, 0.05, 0.10.': {
                        },
                    },
                },
                'Step 3': {
                    'Calculate Test Statistic': {
                        'Depends on the type of test (e.g., t-test, chi-square test).': {
                        },
                    },
                },
                'Step 4': {
                    'Determine Critical Value or p-Value': {
                        'Compare the test statistic with the critical value or use the p-value.': {
                        },
                    },
                },
                'Step 5': {
                    'Make a Decision': {
                        'Reject H0 if the test statistic exceeds the critical value or p<Î±.': {
                        },
                    },
                },
            },
            'Real-World Applications': {
                'Medicine': {
                    'Drug Testing': {
                        'Testing the effectiveness of a new drug.': {
                        },
                    },
                },
                'Manufacturing': {
                    'Quality Control': {
                        'Determining if a production process meets quality standards.': {
                        },
                    },
                },
                'Finance': {
                    'Investment Strategies': {
                        'Evaluating the performance of investment strategies.': {
                        },
                    },
                },
                'Education': {
                    'Teaching Methods': {
                        'Assessing the impact of new teaching methods.': {
                        },
                    },
                },
            },
        },
    },
}