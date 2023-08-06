# 1.功能介绍
---
通过对`docx`和`pyecharts`进行封装，方便快速地生成包含文章主副标题、摘要、多级标题、段落、表格和图片的docx格式word文档。此外，还可以对文本、表格和图片的样式进行修改，生成符合要求的word文档。

通过`pip3 install smartDocx`安装最新包后，即可使用。

如有使用问题, 可至[Github SmartDocx](https://github.com/Sanbomsu/SmartDocx) 反馈。
# 2.目录结构
---
```shell
.
|____package
| |______init__.py
| |____picture.py # 图片
| |____chart.py # 图表
| |____content.py # 文本
| |____paragraph.py # 段落
| |____table.py # 表格
| |____base.py # 基类
| |____title.py # 标题
|____tmp # 临时缓存
|______init__.py
|____report.py # 报告
|____config.py # 全局配置, 包含样式
|____constants.py # 全局常量
|____utils.py # 工具
|____requirements.txt
|____README.md
```
# 3.使用说明
## 3.1 创建/生成报告
---
可以创建全新word文档, 也支持以模板文件基础, 生成副本文档. 
```python
from smartDocx import *
from smartDocx.config import *

# 1.创建文档
# 1.1 创建空文档
report = SmartReportBase(filename="demo.docx", data=dict())

# 1.2 传入模板, 创建新文档
report = SmartReportBase(filename="demo.docx", template="xxx.docx", data=dict())

# 2.渲染文档
report.generate()

#> =================================================================================================
#> 自动化报告开始: /Users/xxx/Storage/xxx/smart-report-svr/demo_20221226175026872286.docx
#> 文章段落结排序结束!
#> 页面设置初始化成功!
#> 页面标题写入成功!
#> 页面副标题写入成功!
#> 文章摘要写入成功!
#> 文章段落内容处理开始!
#> 报告保存本地成功!
#> 清理缓存文件结束!
#> 输出文件: /Users/xxx/Storage/xxx/smart-report-svr/demo_20221226175026872286.docx
#> 
```

## 3.2 标题
---
### 3.2.1 文章标题
```python
paper_title = Title(config=PaperTitleStyleBase())
title.generate(doc_obj=report.doc_obj, text="这是文章标题")
```
### 3.2.2 文章副标题
```python
paper_sub_title = Title(config=PaperSubTitleStyleBase())
title.generate(doc_obj=report.doc_obj, text="这是文章副标题")
```
### 3.2.3 一级标题
```python
first_level_title = Title(config=FirstTitleStyleBase())
first_level_title.generate(doc_obj=report.doc_obj, text="一、这是一级标题")
```
### 3.2.4 二级标题
```python
seconde_level_title = Title(config=SecondTitleStyleBase())
seconde_level_title.generate(doc_obj=report.doc_obj, text="1.1 这是二级标题")
```
### 3.2.5 三级标题
```python
third_level_title = Title(config=ThirdTitleStyleBase())
third_level_title.generate(doc_obj=report.doc_obj, text="1.1.1 这是三级标题")
```
#### 3.2.6 四级标题
```python
fourth_level_title = Title(config=FourthTitleStyleBase())
fourth_level_title.generate(doc_obj=report.doc_obj, text="1.1.1.1 这是四级标题")
```
## 3.3 摘要/正文
---
### 3.3.1 文章摘要
```python
abstract = Paragraph(config=AbstractStyleBase())
abstract.generate(doc_obj=report.doc_obj, text="这是摘要")
```
### 3.3.2 正文(段落)
```python
content = Paragraph(config=ContentStyleBase())
content.generate(doc_obj=report.doc_obj, text="这是正文段落")
```
## 3.3 表格
### 3.3.1 创建
```python
# 表格标题
table_title = Content(config=TableTitleStyleBase())
table_title.generate(doc_obj=report.doc_obj, text="表1.1 这是表1.1的标题")

# 创建表格
table = Table(config=TableBodyStyleBase(), head_config=TableHeadStyleBase())
table_data = dict(
	columns = ["排名", "学号", "成绩"],
	data = [
		(1, 20220101, 95),
		(2, 20220102, 90),
		(3, 20220103, 80)
	]
)
table.generate(doc_obj=report.doc_obj, **table_data)
```
### 3.3.1 单元格高宽
自适应。
### 3.3.2 单元格合并
自动合并相邻值相同的单元格, 可以通过参数`max_merge_col_index`,`horizontal_merge`和`vertical_merge`控制合并范围.
```python
# 位于smartDocx.package.table
class Table(Base):  
    """表格"""  
  
    def __init__(self, config: DocStylesBase, content_type: str = 'TABLE', *args, **kwargs):  
        super(Table, self).__init__(content_type=content_type, config=config, *args, **kwargs)  
        self.body_styles = self.styles  
        if kwargs.get('head_config'):  
            head_config = kwargs['head_config']  
            self.head_styles = head_config._to_dict() if isinstance(head_config, DocStylesBase) else head_config  
        else:  
            self.head_styles = self.body_styles  
        self.column_width_dict = None  
        self.table_head_width_dict = None  
        self.table = None  
        self.columns = None  
        self.data = None  
        self.max_merge_col_index = None  
        self.doc_obj = None  
  
    def generate(self, doc_obj: DocObject, columns: list, data: list, table_title: str = None,  
                 table_title_style: DocStylesBase = None, built_table_color_style: str = '',  
                 max_merge_col_index: int = None, horizontal_merge=True, vertical_merge=True):  
        """  
        生成表格  
        :param doc_obj:        
        :param columns: 表头列表  
        :param data: 标题数据  
        :param table_title: 表格标题  
        :param table_title_style: 表格标题样式  
        :param built_table_color_style: 内置表格样式  
        :param max_merge_col_index: 合并单元格作用最大  
        :param horizontal_merge: 水平方向合并单元格  
        :param vertical_merge: 垂直方向合并单元格  
        :return:       
        """
        ...
        
```
## 3.4 图片
### 3.4.1 插入图片
```python
# 图片配置PicImgStyleBase
# 缩放比例zoom_rate: 默认为1(0~1)
# 对齐方式alignment: 默认DocAlignment.center(居中对齐)
picture = Picture(config=PicImgStyleBase())  
# 图片本地路径pic_path
picture.generate(doc_obj=self.doc_obj, pic_path=pic_path)
```
### 3.4.2 插入echarts图
```python
from smartDocx import Chart
from pyecharts.charts import Map

# 1.创建pyecharts对象
chart_obj = Map()
# 参考文档及链接  
# pyecharts  
# 官网文档: https://pyecharts.org/#/zh-cn/intro  
# 官方示例: https://gallery.pyecharts.org/#/README  
#
# echarts  
# 官方文档: https://echarts.apache.org/zh/feature.html  
# 官方示例: https://echarts.apache.org/examples/zh/index.html
pass

# 2.渲染echarts图片
chart = Chart()
chart.chart_obj = chart_obj
pic_path = chart.render()

# 3.插入图片
picture = Picture(config=PicImgStyleBase())  
picture.generate(doc_obj=self.doc_obj, pic_path=pic_path)
```
>可以使用本地`js`文件, 例如`Map(init_opts=InitOpts(js_host=os.path.join(dir_path, "js/")))`, 解决网络请求超时问题, 或者自定义js事件。以下js文件夹结构，可供参考:
- **RootDirectory**
	- **js**
		- **maps**
			- <u>china.js</u>
		- <u>echarts.min.js</u>

## 3.5 样式
位于`smartDocx.config`, 继承后可自行更改。
```python

class DocStylesBase(object):  
    """文档样式基类"""  
  
    def __init__(self, **kwargs):  
        for k, v in kwargs.items():  
            setattr(self, k, v)  
  
    def _to_dict(self):  
        """转字典"""  
        styles = dict()  
        for attr in dir(self):  
            if attr.startswith('_'):  
                continue  
            value = getattr(self, attr)  
            # 自定义的Enum类型,需转成实际数值  
            if isinstance(value, (DocFontFamily, DocAlignment, TableLandscapeAlignment,  
                                  TableVerticalAlignment, DocFontSize, Orientation)):  
                value = value.value  
            styles[attr] = value  
        return styles  
  
    def __iter__(self):  
        for attr in self._to_dict():  
            yield attr  
  
    def __getitem__(self, item):  
        return self._to_dict()[item]  
  
  
```
### 3.5.1 页面基本属性
```python

class PageStyleBase(DocStylesBase):  
    """页面样式基类"""  
  
    def __init__(self,  
                 page_width: (float, int) = 21.00,  
                 page_height: (float, int) = 29.70,  
                 left_margin: (int, float) = 3.17,  
                 right_margin: (int, float) = 3.17,  
                 top_margin: (int, float) = 2.54,  
                 bottom_margin: (int, float) = 2.54,  
                 orientation: Orientation = Orientation.portrait,  
                 **kwargs):  
        """  
        :param page_width: 页面宽度  
        :param page_height: 页面高度  
        :param left_margin: 左边距cm  
        :param right_margin: 右边距cm  
        :param top_margin: 上边距cm  
        :param bottom_margin: 底边距cm  
        :param orientation: 纸张方向: 默认纵向portrait  
        :param kwargs:        """        
        super(PageStyleBase, self).__init__(  
            page_width=page_width,  
            page_height=page_height,  
            left_margin=left_margin,  
            right_margin=right_margin,  
            top_margin=top_margin,  
            bottom_margin=bottom_margin,  
            orientation=orientation,  
            **kwargs)

```
### 3.5.2 标题
```python

class TitleStyleBase(DocStylesBase):  
    """标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.Four,  
                 text_align=DocAlignment.justify,  
                 font_weight=False,  
                 color='#000000',  
                 font_type=DocFontFamily.MSYH,  
                 west_font_type=DocFontFamily.MSYH,  
                 level=1,  
                 line_indent=False,  
                 line_spacing=None,  
                 style='Normal',  
                 space_before=5,  
                 space_after=5,  
                 italic=False,  
                 underline=0,  
                 **kwargs):  
        """  
        :param font_size: 字体大小  
        :param text_align: 对齐模式  
        :param font_weight: 字体粗细  
        :param color: 字体颜色  
        :param font_type: 中文字体类型  
        :param west_font_type: 西文字体类型  
        :param level: 标题等级  
        :param line_indent: 首航缩进  
        :param line_spacing: 行间距  
        :param style: 字体类型  
        :param space_before: 段前间距  
        :param space_after: 段后间距  
        :param italic: 是否斜体  
        :param underline: 下划线  
        :param kwargs:        """        
        super(TitleStyleBase, self).__init__(  
            font_size=font_size,  
            text_align=text_align,  
            font_weight=font_weight,  
            color=color,  
            font_type=font_type,  
            west_font_type=west_font_type,  
            level=level,  
            line_indent=line_indent,  
            line_spacing=line_spacing,  
            style=style,  
            space_before=space_before,  
            space_after=space_after,  
            italic=italic,  
            underline=underline,  
            **kwargs)


class PaperTitleStyleBase(TitleStyleBase):  
    """文章标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.SmallTwo,  
                 text_align=DocAlignment.center,  
                 font_weight=True,  
                 level=0,  
                 line_spacing=1.5,  
                 space_before=10,  
                 **kwargs):  
        super(PaperTitleStyleBase, self).__init__(  
            font_size=font_size,  
            text_align=text_align,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            **kwargs)


class PaperSubTitleStyleBase(TitleStyleBase):  
    """文章副标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.SmallFour,  
                 text_align=DocAlignment.center,  
                 font_weight=True,  
                 level=0,  
                 line_spacing=1.5,  
                 space_before=10,  
                 **kwargs):  
        super(PaperSubTitleStyleBase, self).__init__(  
            font_size=font_size,  
            text_align=text_align,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            **kwargs)


class FirstTitleStyleBase(TitleStyleBase):  
    """段落: 一级标题样式基类"""  
  
    def __init__(self,  
                 font_weight=True,  
                 level=1,  
                 line_spacing=1.5,  
                 space_before=10,  
                 **kwargs):  
        super(FirstTitleStyleBase, self).__init__(  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            **kwargs)  
  
  
class SecondTitleStyleBase(TitleStyleBase):  
    """段落: 二级级标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.Four,  
                 font_weight=True,  
                 level=2,  
                 line_spacing=1.5,  
                 space_before=5,  
                 **kwargs):  
        super(SecondTitleStyleBase, self).__init__(  
            font_size=font_size,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            **kwargs)  
  
  
class ThirdTitleStyleBase(TitleStyleBase):  
    """段落: 三级标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.SmallFour,  
                 font_weight=True,  
                 level=3,  
                 line_spacing=1.5,  
                 space_before=10,  
                 **kwargs):  
        super(ThirdTitleStyleBase, self).__init__(  
            font_size=font_size,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            **kwargs)  
  
  
class FourthTitleStyleBase(TitleStyleBase):  
    """段落: 四级标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.Five,  
                 font_weight=True,  
                 level=4,  
                 line_spacing=1.5,  
                 space_before=10,  
                 **kwargs):  
        super(FourthTitleStyleBase, self).__init__(  
            font_size=font_size,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            **kwargs)

```
### 3.5.3 段落/摘要
```python

class AbstractStyleBase(ContentStyleBase):  
    """摘要样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.SmallFour,  
                 font_weight=True,  
                 font_type=DocFontFamily.KT,  
                 west_font_type=DocFontFamily.MSYH,  
                 line_spacing=1,  
                 space_before=10,  
                 space_after=30,  
                 **kwargs):  
        super(AbstractStyleBase, self).__init__(  
            font_size=font_size,  
            font_weight=font_weight,  
            font_type=font_type,  
            west_font_type=west_font_type,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            space_after=space_after,  
            **kwargs)


class ParagraphStyleBase(DocStylesBase):  
    """段落样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.SmallFour,  
                 text_align=DocAlignment.justify,  
                 font_weight=False,  
                 color='#000000',  
                 font_type=DocFontFamily.MSYH,  
                 west_font_type=DocFontFamily.MSYH,  
                 line_indent=True,  
                 line_spacing=None,  
                 style='Normal',  
                 space_before=5,  
                 space_after=5,  
                 italic=False,  
                 **kwargs):  
        super(ParagraphStyleBase, self).__init__(  
            font_size=font_size,  
            text_align=text_align,  
            font_weight=font_weight,  
            color=color,  
            font_type=font_type,  
            west_font_type=west_font_type,  
            line_indent=line_indent,  
            line_spacing=line_spacing,  
            style=style,  
            space_before=space_before,  
            space_after=space_after,  
            italic=italic,  
            **kwargs)

```
### 3.5.4 表格
```python

class TableStyleBase(DocStylesBase):  
    """表格样式基类"""  
  
    def __init__(self,  
                 alignment=TableLandscapeAlignment.center,  
                 vertical_alignment=TableVerticalAlignment.center,  
                 font_size=DocFontSize.Five,  
                 font_type=DocFontFamily.MSYH,  
                 west_font_type=DocFontFamily.MSYH,  
                 font_weight=False,  
                 color='#000000',  
                 italic=False,  
                 underline=0,  
                 autofit=True,  
                 background=None,  
                 **kwargs):  
        """  
  
        :param alignment: 水平对齐方式  
        :param vertical_alignment: 垂直对齐方式  
        :param font_size:        
        :param font_type:        
        :param west_font_type:        
        :param font_weight:        
        :param color:        
        :param italic:        
        :param underline:        
        :param autofit: 自动单元格宽度  
        :param background: 单元格背景色  
        :param kwargs:        """        
        super(TableStyleBase, self).__init__(  
            alignment=alignment,  
            vertical_alignment=vertical_alignment,  
            font_size=font_size,  
            font_type=font_type,  
            west_font_type=west_font_type,  
            font_weight=font_weight,  
            color=color,  
            italic=italic,  
            underline=underline,  
            autofit=autofit,  
            background=background,  
            **kwargs)  
  
  
class TableTitleStyleBase(TitleStyleBase):  
    """表格标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.Five,  
                 text_align=DocAlignment.center,  
                 font_weight=True,  
                 level=None,  
                 line_spacing=1.5,  
                 space_before=5,  
                 space_after=0,  
                 underline=0,  
                 background=None,  
                 **kwargs):  
        super(TableTitleStyleBase, self).__init__(  
            font_size=font_size,  
            text_align=text_align,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            space_after=space_after,  
            underline=underline,  
            background=background,  
            **kwargs)  
  
  
class TableHeadStyleBase(TitleStyleBase):  
    """表格首部样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.Five,  
                 font_weight=True,  
                 level=None,  
                 line_spacing=1.5,  
                 space_before=5,  
                 space_after=0,  
                 background=None,  
                 **kwargs):  
        super(TableHeadStyleBase, self).__init__(  
            font_size=font_size,  
            font_weight=font_weight,  
            level=level,  
            line_spacing=line_spacing,  
            space_before=space_before,  
            space_after=space_after,  
            background=background,  
            **kwargs)  
  
  
class TableBodyStyleBase(TableStyleBase):  
    """表格内容样式基类"""  
  
    def __init__(self, **kwargs):  
        super(TableBodyStyleBase, self).__init__(**kwargs)
```
### 3.5.5 图片
```python

class PicTitleStyleBase(TitleStyleBase):  
    """图片标题样式基类"""  
  
    def __init__(self,  
                 font_size=DocFontSize.Five,  
                 level=None,  
                 **kwargs):  
        super(PicTitleStyleBase, self).__init__(  
            font_size=font_size,  
            level=level,  
            **kwargs)  
  
  
class PicImgStyleBase(DocStylesBase):  
    """图片样式基类"""  
  
    def __init__(self,  
                 zom_rate=1,  
                 alignment=DocAlignment.center,  
                 **kwargs):  
        """  
  
        :param zom_rate: 缩放比例  
        :param alignment: 对齐方式  
        :param kwargs:        """        
        super(PicImgStyleBase, self).__init__(  
            zom_rate=zom_rate,  
            alignment=alignment,  
            **kwargs)
```
## 3.6 其他
---
### 3.6.1 换行
`report.lines_break(lines=1)`
### 3.6.2 换页
`report.page_break()`
### 3.6.3 旋转页面
```python
# 页面旋转90度, 例如垂直转水平
report.rotate_page_orientation(orientation=Orientation.landscape)
# 恢复原旋转方向, 例如水平转垂直
report.rotate_page_orientation(orientation=Orientation.portrait)
```
>注意: 页面旋转后, 如果不及时恢复旋转方向, 后续页继承上一页方向。
### 3.6.4 目录页
- 方法一
	- 建议使用已设置好目录的文档作为模板, 写入数据后手动打开刷新;
- 方法二
	- win平台代码打开word自动刷新后保存文档;
### 3.6.5 页眉页脚
docx不支持复杂的页眉页脚设置, 建议使用已设置好页眉页脚的文档作为模板。
### 3.6.6 段落数据快速填充
```python
from smartDocx import SmartReportBase, handle_paragraph, ...


class ReportData(object):

	def __init__(self):
		self.data = dict()

	def chapter_01_paragraph_01(self):
		"""第1章 第1段落"""
		self.data['chapter_01_paragraph_01'] = dict(...)
	...
	def chapter_02_01_paragraph_01(self):
		"""第2章2.1节 第1段落"""
		self.data['chapter_02_01_paragraph_01'] = dict(...)
	...
	def chapter_02_02_01_paragraph_01(self):
		"""第2章2.2.1节 第1段落"""
		self.data['chapter_02_02_01_paragraph_01'] = dict(...)
	
class Report(SmartReportBase):

	@handle_paragraph
	def chapter_01_paragraph_01(self):
		paragraph_data = self.get_paragraph_data() # 效果等同于ReportData().data['chapter_01_paragraph_01']
		...

	@handle_paragraph
	def chapter_02_01_paragraph_01(self):
		paragraph_data = self.get_paragraph_data()
		...

	@handle_paragraph
	def chapter_02_01_paragraph_01(self):
		paragraph_data = self.get_paragraph_data()
		...
	...
```
