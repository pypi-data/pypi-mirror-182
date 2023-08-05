# Test-_repo_rlms
# Open google colab
[GoogleColab](https://colab.research.google.com/)

# Under the section Runtime --> Change runtime --> GPU

![alt text](https://github.com/funnyPhani/Test_repo_rlms/blob/main/img/Screenshot%20(329).png)
![alt text](https://github.com/funnyPhani/Test_repo_rlms/blob/main/img/Screenshot%20(330).png)
![alt text](https://github.com/funnyPhani/Test_repo_rlms/blob/main/img/Screenshot%20(331).png)

# System archiecture of RLMS
![alt text](https://github.com/funnyPhani/Test_repo_rlms/blob/main/img/mainarc-crop.jpg)

# Check the gpu version
```python
!nvidia-smi
```
![alt text](https://github.com/funnyPhani/Test_repo_rlms/blob/main/img/Screenshot%20(332).png)

# Clone the repo to the colab notebook
```python 
!git clone https://github.com/funnyPhani/Test_repo_rlms/
```

# Install the required packages for RLMS
```python

!pip install -r /content/Test_repo_rlms/requirements.txt
```
## Change directory
```python
!cp /content/Test_repo_rlms/rlms.py /content

```

```python
cd /content
```
![alt text](https://github.com/funnyPhani/Test_repo_rlms/blob/main/img/Screenshot%20(333).png)

# To test the rlms approach
[Miltimodal news data to test RLMS](https://www.voanews.com/)
```python
from rlms import get_summary_multioutput
get_summary_multioutput()

```



[Our Colab Link to test](https://colab.research.google.com/drive/1tZ_z8owh6_d8gN7ClIrmIEg5ngEvNevk?usp=sharing)

