import nose
from selenium.webdriver import ActionChains


from Browser import Browser

link = "https://qavbox.github.io/demo/dragndrop/"
objectToDrag = "draggable"
objectToDrop = "droppable"
sliderb = '/html[1]/body[1]/form[1]/fieldset[1]/div[1]/div[5]/input[1]'


class drag_drop(Browser):
    @nose.allure.severity(nose.allure.severity_level.CRITICAL)

    def drag(self):
        source_element = self.driver.find_element_by_id(objectToDrag)
        dest_element = self.driver.find_element_by_id(objectToDrop)
        ActionChains(self.driver).drag_and_drop(source_element, dest_element).perform()

    def result(self):
        success_msg = self.driver.find_element_by_id("dropText").text
        return success_msg

    def setup(self):
        self.driver.get(link)

    def slider(self):
        slider = self.driver.find_element_by_xpath(sliderb)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 280, 16).perform()

    def verif_slider(self):
        success_msg = self.driver.find_element_by_id("range").text
        return success_msg
