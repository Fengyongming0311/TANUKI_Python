__author__ = 'TANUKI'
#coding:utf-8

import requests, xlrd, time, sys
from xlutils import copy
#从xlutils模块中导入copy这个函数

Base = "218.28.28.186"
Port = '9088'

class Runinterface:
    def readExcel(file_path):
        '''
        :param file_path: 导入excel的路径
        :return:None
        '''
        try:
            book = xlrd.open_workbook(file_path)#打开excel
        except Exception as e:
        #如果路径不在或者excel不正确，返回报错信息
            print ('路径不在或者excel不正确',e)
            return e
        else:
            sheet = book.sheet_by_index(0)   #取第一个sheet页
            rows= sheet.nrows  #取这个sheet页的所有行数
            case_list = []#保存每一条case
            for i in range(rows):
                #把第一条标题行排除了
                if i != 0:
                    #把每一条测试用例添加到case_list中
                    case_list.append(sheet.row_values(i))
            #调用接口测试的函数，把存所有case的list和excel的路径传进去，因为后面还需要把返回报文和测试结果写到excel中，
            #所以需要传入excel测试用例的路径，interfaceTest函数在下面有定义
            Runinterface.interfaceTest(case_list,file_path)
            #上面的把Excel中的值传到下面的interfaceTest，然后interfaceTest进行接口测试

        #print (case_list)


    def interfaceTest(case_list, file_path):
        '''
        :param case_list: 把从excel中读取出来的数据放到方法里进行接口操作
        :param file_path: 目前还没用到
        :return:
        '''
        res_flags = []
        #存测试结果的list
        request_urls = []
        #存请求报文的list
        responses = []
        #存返回报文的list

        for case in case_list:
            '''
            先遍历excel中每一条case的值，然后根据对应的索引取到case中每个字段的值
            '''
            try:
                """
                这里捕捉一下异常，如果excel格式不正确的话，就返回异常
                """
                case_id = case[0]
                #用例id，提bug的时候用
                testcase = case[1]
                #用例描述，实际测试用例
                interface_name = case[2]
                #接口名称，也是提bug的时候用
                case_detail = case[3]
                #用例描述
                method = case[4]
                #请求方式
                url = "http://" + Base + ":" + Port + "/ehomeapp/app" + case[5]
                #请求url地址改这里
                param = case[6]
                #入参
                res_check = case[7]
                #预期结果
                tester = case[10]
                #测试人员
            except Exception as e:
                return '测试用例格式不正确！%s'%e


            print ("执行用例:",case_id,"用例名称:",case_detail)

            if param== '':
                '''
                如果请求参数是空的话，请求报文就是url，然后把请求报文存到请求报文list中
                '''
                new_url = url#请求报文
                request_urls.append(new_url)

            else:
                '''''
                如果请求参数不为空的话，请求报文就是url+?+参数，格式和下面一样
                http://127.0.0.1:8080/rest/login?oper_no=marry&id=100，然后把请求报文存到请求报文list中
                '''
                new_url = url+'?'+Runinterface.urlParam(param)#请求报文
                print ("请求报文为：",new_url)
                '''
                excel里面的如果有多个入参的话，参数是用;隔开，a=1;b=2这样的，请求的时候多个参数要用&连接，
                要把;替换成&，所以调用了urlParam这个函数，把参数中的;替换成&，函数在下面定义的
                '''
                request_urls.append(new_url)
            #Python upper() 方法将字符串中的小写字母转为大写字母。
            if method.upper() == 'GET':
                '''
                如果是get请求就调用requests模块的get方法，.text是获取返回报文，保存返回报文，
                把返回报文存到返回报文的list中
                '''
                results = requests.get(new_url).text
                print ("返回结果为",results)
                responses.append(results)
                #print (interface_name,"返回结果为",responses)
                '''
                获取到返回报文之后需要根据预期结果去判断测试是否通过，调用查看结果方法
                把返回报文和预期结果传进去，判断是否通过，readRes方法在下面定义了。
                '''

            elif method.upper() == 'POST':
                '''
                如果不是get请求，也就是post请求，就调用requests模块的post方法，.text是获取返回报文，
                保存返回报文，把返回报文存到返回报文的list中
                '''
                results = requests.post(new_url).text
                print ("返回结果为",results)
                responses.append(results)
                #print (interface_name,"返回结果为",responses)



            else:
                print ("老铁，请求方式的英文你拼错了吧...")


            #下面验证是否测试通过调用readRes方法
            res = Runinterface.readRes(results,res_check)
            print (res)



    def readRes(res, res_check):
        '''
        :param res: 返回报文
        :param res_check: 预期结果
        :return: 通过或者不通过，不通过的话会把哪个参数和预期不一致返回
        '''
        #先做数据清洗，变成{"code":"1000","data":[],"message":"信息已获取"}
        res = res.replace('":"',"=").replace('":',"=")
        res = res.strip("{}")

        if res_check in res:
            return "PASS"
        else:
            return "错误，返回参数和预期结果不一致==================>>>" + res_check


    def urlParam(param):
        '''
        参数转换，把参数转换为'xx=11&xx=2这样'
        '''
        return param.replace(';','&')

    def copy_excel(file_path,res_flags,request_urls,responses):
        '''''
        :param file_path: 测试用例的路径
        :param res_flags: 测试结果的list
        :param request_urls: 请求报文的list
        :param responses: 返回报文的list
        :return:
        '''
        '''''
        这个函数的作用是写excel，把请求报文、返回报文和测试结果写到测试用例的excel中
        因为xlrd模块只能读excel，不能写，所以用xlutils这个模块，但是python中没有一个模块能
        直接操作已经写好的excel，所以只能用xlutils模块中的copy方法，copy一个新的excel，才能操作
        '''

        book = xlrd.open_workbook(file_path)
        #打开原来的excel，获取到这个book对象
        new_book = copy.copy(book)
        #复制一个new_book
        sheet = new_book.get_sheet(0)
        #然后获取到这个复制的excel的第一个sheet页
        i = 1
        '''
        同时遍历请求报文、返回报文和测试结果这3个大的list
        然后把每一条case执行结果写到excel中，zip函数可以将多个list放在一起遍历
        因为第一行是表头，所以从第二行开始写，也就是索引位1的位置，i代表行
        所以i赋值为1，然后每写一条，然后i+1， i+=1同等于i=i+1
        请求报文、返回报文、测试结果分别在excel的8、9、11列，列是固定的，所以就给写死了
        后面跟上要写的值，因为excel用的是Unicode字符编码，所以前面带个u表示用Unicode编码
        否则会有乱码
        '''
        sheet.write(i,8,u'%s'%request_url)
        sheet.write(i,9,u'%s'%response)
        sheet.write(i,11,u'%s'%flag)





if __name__ == '__main__':
    filename = 'Hachi.xlsx'
    try:
        Runinterface.readExcel(filename)

        #print ("Done!")
    except Exception as e:
        print (e)

