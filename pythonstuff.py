def reorder(string):
  first = string[0:1]
  middle = string[1:len(string)-1]
  end = string[len(string)-1:len(string)]
  newstring = end + middle + first
  return newstring

print("\n\nMEOW should be printed as WEOM")
meow = reorder('MEOW')
print(meow)


print("\n\nGIRKGBSDKG should be returned as GIRKGBSDKG")
girkgbsdkg = reorder("GIRKGBSDKG")
print(girkgbsdkg)

print("\n\nHIIII should be returned as IIIIH")
hi = reorder('HIIII')
print(hi + "\n\n")
