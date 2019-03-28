import allure
class Test_1:

    @allure.step(title="测试步骤001")
    def  test_001(self):
        allure.attach("测试标题","测试描述",allure.attach_type.TEXT)
        print("12132")
        assert True
    def test_002(self):
        with open("./1.jpg","rb") as f:
          allure.attach("图片",f.read(),allure.attach_type.JPG)
        assert True