r=int(input("enter the radius of the cylinderical part"))
h=int(input("enter the height of the cylindrical part"))
def cyl_part(r,h):
    csa=2*3.14*r*h
    return csa

l=int(input("enter the slant height of the cone"))
def con_part(l,r):
    csa_cone=3.14*r*l
    return csa_cone
total_area=float(cyl_part(r,h)+con_part(l,r))
print("the total area for the canvas",total_area)
unit_price=float(input("enter the amt for 1m^2 canvas"))
payamt=total_area*unit_price
print("amt payable for the canvas excluding gst is:",payamt)
gst=0.18
final_amt=payamt*gst+payamt
print("amt payable for the canvas including gst is:",final_amt)
