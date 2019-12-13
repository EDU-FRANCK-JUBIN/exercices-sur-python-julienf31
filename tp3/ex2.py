from pyDatalog import  pyDatalog

pyDatalog.create_terms('X,Y,triangle,nb_cotes,cotes_egaux,angle_droit,triangle_rectangle','triangle_isocele','triangle_equilateral','triangle_rectangle_isocele')
#pyDatalog.create_atoms('croakes','eatFlies','frog','chirps','sings','canary','green','yellow')

triangle(X) <= nb_cotes(X,Y) & (Y==3)
triangle_rectangle(X) <= triangle(X) & angle_droit(X)
triangle_isocele(X) <= triangle(X) & cotes_egaux(X,Y) & (Y==2)
triangle_equilateral(X) <= triangle(X) & cotes_egaux(X,Y) & (Y==3)
triangle_rectangle_isocele(X) <= triangle_rectangle(X) & cotes_egaux(X,Y) & (Y==2)


+nb_cotes('polygone_1',3)
+nb_cotes('polygone_2',4)
+nb_cotes('polygone_3',3)

+angle_droit('polygone_1')
+cotes_egaux('polygone_3',2)
+cotes_egaux('polygone_1',2)

print("Triangle :",pyDatalog.ask('triangle(X)').answers)
print("Triangle rectangle :",pyDatalog.ask('triangle_rectangle(X)').answers)
print("Triangle rectangle isocele :",pyDatalog.ask('triangle_rectangle_isocele(X)').answers)
print("Triangle isocéles :",pyDatalog.ask('triangle_isocele(X)').answers)
