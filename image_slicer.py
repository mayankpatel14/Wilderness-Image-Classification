for i in input_images_list:
    input_image_path = os.path.join(input_path, i)
    img = Image.open(input_image_path)
    img_arr = np.array(img)
    
    output_image_path=os.path.join(output_path, i[:-4])
    
    k=0 
    for r in range(0,2822,256):
        for c in range(0,4800,256):
            if c+256<4800 and r+256<2903:
                im = Image.fromarray(img_arr[r:r+256,c:c+256,:])
                im.save(output_image_path+'/' + str(k) + ".jpg")
                k+=1
                print(i,k)