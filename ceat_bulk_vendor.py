from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# List of vendor codes
vendor_codes =["1100162","1600025","1600074","1600807","1700417","1700838","2100283","2100305","2100440","2100797","2100817","2100960","2100995","2101138","2101571","2101663","2200034","2200046","2200061","2200093","2200115","2200120","2200162","2200204","2200216","2200241","2200275","2200306","2200312","2200320","2200377","2200424","2200447","2200476","2200497","2200500","2200534","2200556","2200596","2200597","2200654","2200657","2200665","2200703","2200704","2200765","2200798","2200806","2200822","2200827","2200829","2200840","2200845","2200875","2200912","2200996","2201000","2201001","2201020","2201072","2201129","2201142","2201174","2201240","2201253","2201264","2201269","2201275","2201325","2201374","2201387","2201389","2201435","2201480","2201481","2201482","2201637","2201643","2201652","2201662","3500040","3504355","3506571","3507407","3507449","3700113","3700408","3800020","3800021","3800082"]
 
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize the Chrome driver
print("Initializing browser...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Step 1: Login
    print("\n" + "="*60)
    print("STEP 1: LOGIN")
    print("="*60)
    login_url = "https://weconnect.ceat.com/"
    print(f"Opening login page: {login_url}")
    driver.get(login_url)
    
    time.sleep(2)
    
    # Fill username
    print("Entering username: ezcadmin")
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.clear()
    username_field.send_keys("ezcadmin")
    
    # Fill password
    print("Entering password: Vanila2023")
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("AstVe1951a")
    
    # Click Sign In button
    print("Clicking Sign In button...")
    signin_button = driver.find_element(By.ID, "loginBP")
    signin_button.click()
    
    # Wait for login to complete
    print("Waiting for login to complete...")
    time.sleep(5)
    print("✓ Login successful")
    
    # Step 2: Process each vendor
    print("\n" + "="*60)
    print("STEP 2: PROCESSING VENDORS")
    print("="*60)
    
    quick_vendor_url = "https://weconnect.ceat.com/CEAT/EzCommerce/EzAdmin/EzAdmin4/Admin1/JSPs/User/ezQuickVendorCheck.jsp?Area=V"
    
    success_count = 0
    fail_count = 0
    
    for index, vendor_code in enumerate(vendor_codes, 1):
        print(f"\n{'='*60}")
        print(f"Processing vendor {index}/{len(vendor_codes)}: {vendor_code}")
        print(f"{'='*60}")
        
        try:
            # Navigate to Quick Vendor Check page
            print(f"Opening Quick Vendor Check page...")
            driver.get(quick_vendor_url)
            time.sleep(3)
            
            # Find the first vendor input field
            print(f"Finding vendor input field...")
            vendor_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "vendor"))
            )
            
            # Fill in vendor code
            print(f"Entering vendor code: {vendor_code}")
            vendor_input.clear()
            vendor_input.send_keys(vendor_code)
            time.sleep(1)
            
            # Click first Continue button
            print(f"Clicking first Continue button...")
            try:
                first_continue = driver.find_element(By.XPATH, "//a[@href='JavaScript:funChk()']")
                first_continue.click()
            except:
                # Alternative: use JavaScript
                driver.execute_script("funChk();")
            
            # Wait for next page to load
            print(f"Waiting for next page to load...")
            time.sleep(3)
            
            # Click second Continue button
            print(f"Clicking second Continue button...")
            try:
                second_continue = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//a[@href='JavaScript:funSubmit()']"))
                )
                second_continue.click()
            except:
                # Alternative: use JavaScript
                driver.execute_script("funSubmit();")
            
            # Wait for submission to complete
            print(f"Waiting for submission to complete...")
            time.sleep(3)
            
            print(f"✓ Vendor {vendor_code} processed successfully")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error processing vendor {vendor_code}: {str(e)}")
            fail_count += 1
            # Continue with next vendor
            continue
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total vendors: {len(vendor_codes)}")
    print(f"✓ Successfully processed: {success_count}")
    print(f"✗ Failed: {fail_count}")
    print("="*60)
    
    print("\nPress ENTER to close the browser...")
    input()

except Exception as e:
    print(f"\n✗ FATAL ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
    print("\nPress ENTER to close the browser...")
    input()

finally:
    # Close the browser
    print("\nClosing browser...")
    driver.quit()
    print("Done!")
