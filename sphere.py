radius = float(input("Enter the radius of a sphere: "))
diameter = radius * 2
circumference = round(2 * 3.14 * radius, 2)
area = round(4 * 3.14 * radius ** 2, 2)
volume = round(4 / 3 * 3.14 * radius ** 3, 2)
print("With a radius of", radius, "the diameter of a sphere is ",diameter,".")
print("With a radius of", radius, "the circumference of a sphere is ", circumference,".")
print("With a radius of", radius, "the surface area of a sphere is ", area,".")
print("With a radius of", radius, "the volume of a sphere is ", volume,".")
