## Regular shapes in 3d fractograms
```
Period 6 - Hexagonal: 	[7, 13, 	39, 63, 77, 91,      143, 273,      429, 693, 819,      1001, 1287, 3003, 9009]
Period 3 - Triangular:	[       27, 37,                 111,           333,                999,                   ]
```

All the period 3 fractions shown above can be rewritten in the form n/999, where n is a factor of 999.

999 = 3<sup>3</sup> × 37

1/27  = 37/999 = 0.037037...

1/37  = 3<sup>3</sup>/999 = 0.027027...

1/111 = 3<sup>2</sup>/999 = 0.009009...

1/333 = 3<sup>1</sup>/999 = 0.003003...

1/999 = 3<sup>0</sup>/999 = 0.001001...

H. Duncan showed that all period 3 fractions form equilateral triangles.

---

Consider a period 6 fraction with digits abcdef recurring. It's points are thus:
`(a,b,c)   (b,c,d)   (c,d,e)   (d,e,f)   (e,f,a)   (f,a,b)` then back to `(a,b,c)`

The distances between these points follow a pattern:

√(a-b)² + (b-c)² + (c-d)² then √(b-c)² + (c-d)² + (d-e)² etc...,
 each time taking the last two terms under the root and adding a new one.

For all period 6 fractions with the property that
(a-b)² = (d-e)²
(b-c)² = (e-f)²
(c-d)² = (f-a)²
then all of these terms can be simplified to using the same 3 differences and shown to be equal. QED.




