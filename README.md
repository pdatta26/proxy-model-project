# Proxy Model Project
<p align="center">
  <img src="https://github.com/pdatta26/proxy-model-project/blob/master/proxysql.jpg" width="350" alt="Proxy Model   ">
</p>
In this proxy I have used django roxy model.
The concept of proxy model is making replica of a model.

# How to make a proxy model: 
1. At first need to make a model, in my case <b>Car</b> model.
2. The car model contains 3 fields 
   1. model
   2. brand
   3. wheel <br>
   <i><b> Source code: </b></i>
   
   ```
   class Car(models.Model): 
       model = models.CharField(max_length=100, blank=False, null=False)
       brand = models.CharField(max_length=100, blank=False, null=False)
       wheel = models.CharField(max_length=100, blank=False, null=False)
   ```

3. How to make a proxy model
      1. Create a new model
      2. inherite the new model, from which model you want to make the replica
      3. Write a meta class,  add a property proxy and make it True
      In my case, I have created two new models to make the replica. <br>
      <i><b> Source code: </b></i>
      ```
         class Honda(Car):
             class Meta:
                 proxy = True
         
         class PrivetCar(Car):
             class Meta:
                 proxy = True
      ```
      4. When you make a proxy model, The proxy models will contain all of the parent class data. If you need to make 
      replica based any condition, you must need to create a <b>Model Manager</b> for each proxy model
      

4. How to create a Model Manager
   1. Write a new class and inhrite it from <b>models.Manager</b>.
   2. write a queryset method and apply your condition. <br>
   in my case I want to separate which <b>Car</b> objects are containing model field value as "Honda", Their replica will 
   be created into <b>Honda</b> proxy model, and which containing model field value as "PrivetCar", Their replica will 
   be created into <b>PrivetCar</b> proxy model.
   <br>
   <i><b> Source code: </b></i><br>
   
    ```
       class HondaManager(models.Manager):
           def get_queryset(self):
               return super().get_queryset().filter(model="Honda")


       class PrivetCarManager(models.Manager):
           def get_queryset(self):
               return super().get_queryset().filter(model="PrivetCar")
    ```
   
   3. After that call the new created manager from your proxy model.
   4. How to call a manager from proxy model.<br>
      In may case<br>
      <i><b> Source code: </b></i>
      ```
       class Honda(Car):
           objects = HondaManager()

           class Meta:
               proxy = True


       class PrivetCar(Car):
           objects = PrivetCarManager()

           class Meta:
               proxy = True
      ```
   
      Congratulations, You are done with proxy model.