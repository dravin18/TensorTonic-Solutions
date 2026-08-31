# TensorTonic Solutions

Welcome to my TensorTonic solutions repository!

Here you'll find my solutions to various machine learning and deep learning problems from [TensorTonic](https://tensortonic.com).

## What is TensorTonic?

TensorTonic is a platform where you can implement core algorithms of Machine Learning from scratch.

This repository contains my personal solutions to these problems, automatically synchronized from the platform.

<!-- tensortonic:start -->
# Deepak Somasundaram's TensorTonic Solutions

Verified machine learning implementations completed on [TensorTonic](https://www.tensortonic.com).

<p align="center">
  <img src="https://www.tensortonic.com/api/badge/dravin.svg" alt="TensorTonic Verified Solutions" width="100%" />
</p>

| Problem | Description | Link |
|---|---|---|
| Bernoulli Probability Mass Function & Moments | Compute the Bernoulli probability mass function, expected value, and variance for a valid success probability. | https://www.tensortonic.com/problems/bernoulli-pmf |
| Implement Cosine Similarity | Compute cosine similarity between NumPy vectors with dot products, Euclidean norms, and zero-vector handling. | https://www.tensortonic.com/problems/cosine-similarity |
| Implement Dot Product | Implement the dot product of equal-length numeric vectors by summing element-wise products without library shortcuts. | https://www.tensortonic.com/problems/dot-product |
| Compute Entropy for a Node | Compute decision-tree node entropy from class labels using empirical class probabilities and base-two logarithms. | https://www.tensortonic.com/problems/entropy-node |
| Compute Gini Impurity for a Split | Compute weighted Gini impurity for a candidate decision-tree split from the class labels on both sides. | https://www.tensortonic.com/problems/gini-impurity |
| Gradient Clipping (Global Norm) | Clip a NumPy gradient array by its global L2 norm while preserving direction when scaling is required. | https://www.tensortonic.com/problems/gradient-clipping |
| He Initialization | Scale raw weights into the He uniform range using a bound derived from the layer fan-in. | https://www.tensortonic.com/problems/he-initialization |
| Image Histogram | Count grayscale image pixels into intensity bins and return the histogram in ascending intensity order. | https://www.tensortonic.com/problems/image-histogram |
| K-Means Assignment Step | Assign each sample to its nearest K-means centroid using Euclidean distance and deterministic tie handling. | https://www.tensortonic.com/problems/k-means-assignment |
| Implement Leaky ReLU (with α) | Apply Leaky ReLU element-wise with a configurable negative slope while retaining positive inputs. | https://www.tensortonic.com/problems/leaky-relu |
| Linear Regression Closed Form | Fit linear regression with the closed-form normal equation and return coefficients for the supplied design matrix. | https://www.tensortonic.com/problems/linear-regression-closed-form |
| Implement Majority Class Classifier | Fit a majority-class baseline and predict the most frequent training label for every requested sample. | https://www.tensortonic.com/problems/majority-classifier |
| Matrix Trace | Compute the trace of a square matrix by summing its main diagonal entries without changing the input. | https://www.tensortonic.com/problems/matrix-trace |
| Matrix Transpose | Implement matrix transpose in NumPy without built-in transpose helpers, preserving rectangular shapes and the original input. | https://www.tensortonic.com/problems/matrix-transpose |
| Mean, Median, Mode | Calculate the mean, median, and deterministic mode of a numeric collection, including tied frequencies. | https://www.tensortonic.com/problems/mean-median-mode |
| Percentiles / Quantiles | Calculate requested percentiles from numeric data using the interpolation rule specified by the problem. | https://www.tensortonic.com/problems/percentiles |
| Perplexity Computation | Compute language-model perplexity from token probability distributions and the observed token indices. | https://www.tensortonic.com/problems/perplexity-computation |
| Implement Positional Encoding (sin/cos) | Generate sinusoidal Transformer positional encodings across sequence positions and embedding dimensions. | https://www.tensortonic.com/problems/positional-encoding |
| Prioritized Experience Replay | Compute prioritized replay sampling probabilities and normalized importance weights from transition priorities. | https://www.tensortonic.com/problems/priority-replay-sample |
| Random Forest Majority Vote | Combine multiple decision-tree predictions with majority voting and deterministic handling of tied classes. | https://www.tensortonic.com/problems/random-forest-vote |
| Sample Variance & Standard Deviation | Compute sample variance and standard deviation with Bessel's correction from a numeric collection. | https://www.tensortonic.com/problems/sample-var-std |
| SELU Activation | Apply SELU activation element-wise with scaled positive values and exponential negative values. | https://www.tensortonic.com/problems/selu-activation |
| Streaming Min-Max Normalization | Update per-feature running minima and maxima, then normalize each incoming numeric batch with the new state. | https://www.tensortonic.com/problems/streaming-minmax |
| Implement Swish Activation | Apply the Swish activation element-wise by multiplying each input by its sigmoid value. | https://www.tensortonic.com/problems/swish-activation |
| Xavier Initialization | Scale raw weights into the Xavier uniform range using a bound derived from fan-in and fan-out. | https://www.tensortonic.com/problems/xavier-initialization |
| Image Normalize | Normalize each image channel by its supplied mean and standard deviation to produce standardized vision-model inputs. | https://www.tensortonic.com/study-plans/cracking-cv/cv-image-normalize |
| RGB to Grayscale | Convert an RGB image to grayscale with luminance-weighted color channels for classical computer vision preprocessing. | https://www.tensortonic.com/study-plans/cracking-cv/cv-rgb-to-grayscale |
| KNN Classifier | Implement K-nearest neighbors classification using Euclidean distance, majority voting, and deterministic tie-breaking. | https://www.tensortonic.com/study-plans/cracking-ml/ml-knn-classifier |
| Linear Regression from Scratch | Train linear regression from scratch with mean squared error gradients for weights and bias. | https://www.tensortonic.com/study-plans/cracking-ml/ml-linear-regression-from-scratch |
| Mean, Median, Mode | Compute mean, median, and a deterministically selected mode for a one-dimensional numeric sample. | https://www.tensortonic.com/study-plans/math-probability/probstat-mean-median-mode |
| Aggregation Functions | Compute selected NumPy aggregation functions globally or along a requested axis using float64 values. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-aggregation |
| Angle Features | Return a float64 array where row 0 contains the sine values, row 1 the cosine values, and row 2 the tangent values. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-angle-features |
| Arange and Linspace | Generate a one-dimensional NumPy sequence using either step-based arange or count-based linspace semantics. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-arange-linspace |
| Basic Indexing | Extract a rectangular NumPy subarray with row and column slice boundaries using standard basic indexing. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-basic-indexing |
| Boolean Masking | Build three filtered views of a 2D array: an element-level boolean mask, rows kept when any element exceeds a threshold. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-boolean-masking |
| Column Scaling | Scale every column of a NumPy matrix by its aligned weight through broadcasting, without explicit Python loops. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-col-scaling |
| Create Arrays from Lists | Create NumPy arrays from Python lists with the requested dtype and return their values, shape, dimensions, and element count. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-create-array |
| Fancy Indexing | Convert the data to float64 and return the array formed by selecting elements along that axis using integer array indexing. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-fancy-indexing |
| Filter and Extract | Implement Filter and Extract, and apply a boolean mask to select values strictly greater than threshold. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-filter-extract |
| Mutation Trap | Extract an independent NumPy row copy, mutate it safely, and verify that the original array remains unchanged. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-mutation-trap |
| Normalized Difference | Use two 2D arrays a and b of the same shape and a scalar range [lo, hi], clip both arrays to [lo, hi], rescale each to [0, 1]. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-norm-diff |
| Norm-Gated Linear Transform | Compute the linear transform Z = X @ W, then zero out every row of Z whose L2 norm is strictly below the threshold. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-norm-gate |
| Normalize Columns | Standardize each NumPy matrix column by subtracting its mean and dividing by its population standard deviation. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-normalize-columns |
| Outer Sum | Compute the broadcasted outer sum of two NumPy vectors without loops, supporting different lengths and numeric values. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-outer-sum |
| Pairwise Differences | Implement Pairwise Differences, and compute the pairwise difference matrix without any Python loops. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-pairwise-diff |
| Random Array Generation | Generate seeded float64 NumPy arrays from either a uniform or standard normal distribution. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-random-arrays |
| Reshaping Arrays | Transform a float64 NumPy array with flattening, transposition, or a validated target shape. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-reshape |
| Row Extremes | Implement Row Extremes, using np.argmax(axis=1) to find the column index of the maximum value in each row. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-row-extremes |
| Row Scaling | Scale every row of a NumPy matrix by its aligned weight through broadcasting, without explicit Python loops. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-row-scaling |
| Sort and Argsort | Return NumPy values sorted along a selected axis together with the indices that produce the same ordering. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-sort-argsort |
| Winsorize | Winsorization clips extreme values in each column to percentile-based bounds, a standard technique for suppressing outliers in ML preprocessing. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-winsorize |
| Zeros and Ones | Create a two-dimensional float64 NumPy array of a requested shape filled entirely with zeros or ones. | https://www.tensortonic.com/study-plans/numpy-basics/numpy-zeros-ones |
| Aggregation Functions | Implement Aggregation Functions, and return a dict mapping each function name to a dict of group label to aggregated value. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-aggregation-functions |
| Apply Custom Transforms | Apply a named transformation to one pandas column and store the result in a new derived column. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-apply-custom-functions |
| Boolean Indexing | Filter pandas rows by a numeric column threshold and return the matching records with their original column order. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-boolean-indexing |
| Change Data Types | Create a DataFrame, convert the specified column to the target type, and return the dtypes before and after conversion. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-change-dtypes |
| Column Selection | Create a pandas DataFrame from dictionary data and extract one named column as an ordered list. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-column-selection |
| Concatenate DataFrames | Concatenate multiple pandas DataFrames vertically and return the combined records with a reset index. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-concatenate-dataframes |
| Cross Tabulation | Create a DataFrame and compute a cross-tabulation (frequency table) showing how often each combination of values co-occurs. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-cross-tabulation |
| Data Types Overview | Create a pandas DataFrame and report each column dtype together with counts for every unique dtype. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-data-types |
| Drop Duplicates | Create a DataFrame, remove duplicate rows, and return the cleaned result along with counts of rows before and after deduplication. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-drop-duplicates |
| GroupBy Basics | Create a DataFrame and compute the sum, mean, and count of the value column for each group. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-groupby-basics |
| Handle Missing Values | Create a pandas DataFrame, count missing entries per column, and replace every null with a supplied fill value. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-handle-missing |
| Head and Tail Operations | Create a pandas DataFrame and return the requested first and last rows as record-oriented dictionaries. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-head-tail |
| Inspect DataFrame Shape | Create a DataFrame and return its structural properties: row count, column count, column names, data types, and total number of values. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-inspect-shape |
| Loc vs iLoc | Create a DataFrame and use positional indexing to extract: the single element, the full row, and the full column. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-loc-iloc |
| Melt Wide to Long | Reshape a pandas DataFrame from wide to long format using selected identifier and value columns. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-melt-wide-to-long |
| Merge DataFrames | Use two dictionaries of column data and a key column present in both, create two DataFrames and merge them on the key column using a specified join type. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-merge-dataframes |
| Multi-Column Selection | Create a pandas DataFrame and select an ordered subset of named columns without changing row order. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-multi-column-selection |
| Multi-Level GroupBy | Create a DataFrame, group by all specified columns, apply the aggregation, and return the result as a flat table. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-multi-level-groupby |
| Pivot Tables | Build a pandas pivot table with selected index, columns, values, aggregation, and zero-filled missing combinations. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-pivot-tables |
| Create DataFrame from Dict | Create a pandas DataFrame from dictionary data and report its records, shape, and ordered column names. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-read-csv |
| Rename Columns | Rename selected pandas DataFrame columns from an old-to-new mapping and return the updated records. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-rename-columns |
| Replace Values | Create a DataFrame, replace all occurrences of the old value with the new value in the specified column, and count how many replacements were made. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-replace-values |
| Resetting Index | Set a pandas column as the index, then restore the default integer index while retaining the original values. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-resetting-index |
| Setting Index | Set a named pandas DataFrame column as the index and report the resulting records and index metadata. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-setting-index |
| Unstack Long to Wide | Implement Unstack Long to Wide, and return a dict of lists representing the wide-format DataFrame. | https://www.tensortonic.com/study-plans/pandas-basics/pandas-unstack-long-to-wide |

View my verified ML profile: [TensorTonic profile](https://www.tensortonic.com/profile/dravin)
<!-- tensortonic:end -->
