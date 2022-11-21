import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(
    img,"sun",
    (20,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,"mercury",
    (100,260),
    cv2.FONT_HERSHEY_COMPLEX,
   0.5,
    (255,255,255)

    

)
cv2.putText(
    img,"venus",
    (200,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)

)
cv2.putText(
    img,"earth",
    (300,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,"mars",
    (400,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,"jupiter",
    (500,350),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,"saturn",
    (690,260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(
    img,"uranus",
    (950,260),
    cv2.FONT_HERSHEY_COMPLEX,
  
    0.5,
    (255,255,255)
)
cv2.putText(
    img,"neptune",
    (960,260),
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.imwrite("solar_systemwithName.jpg",img),
    0.5,
    (255,255,255)
)


cv2.imshow("output",img)
cv2.waitKey(0)