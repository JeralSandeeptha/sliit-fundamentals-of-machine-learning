# DBSCAN Clustering

`Density-Based Clustering` is an unsupervised machine learning method that groups data points together based on how closely packed they are in space.

- It can identify noices in clusters

![Image](../../images/dbscan-01.png)

<br/>

## How It Works

- Core Point - Have MinPoints or More than
- Border Point - Have Less than MinPoints
- Noise Point - No Points

<br/>

EPS = 2 (Circle Radius Value) / (Epsilon Value)
MinPoints = 3

![Image](../../images/dbscan-02.png)
![Image](../../images/dbscan-03.png)
![Image](../../images/dbscan-04.png)

That's how they cluster data points
