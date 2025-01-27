# eazy version

# largest = a
# if b > largest then:
#     largest = b
# end if

# if c > largest then:
#     largest = c
# end if
# if e > largest then:
#     largest = e
# end if
# return largest

# ----------------------------------------------------------------

# if a > b then
#     if a > c then
#         if a > e then
#             return a
#         end if
#     else
#         if c > e then
#             return c
#         else
#             return e
#         end if
#     end if
# else
#     if b > c then
#         if b > e then
#             return b
#         else
#             return e
#         end if
#     else
#         if c > e then
#             return c
#         else
#             return e
#         end if
#     end if
# end if