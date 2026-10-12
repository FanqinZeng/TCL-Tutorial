"""Render six original captioned code demonstrations from real native Tcl output.

macOS: WORKSHOP_USE_TK=1 python3 scripts/render_media.py --encode
Frames are generated locally with Pillow; Swift/AVFoundation writes H.264 MP4.
No browser actions, interpreter results, or third-party footage are fabricated.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
from PIL import Image, ImageDraw, ImageFont
from check import native

ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / 'site' / 'media'
WIDTH, HEIGHT, HOLD, FPS = 1280, 720, 5, 2
FONT_PATH = os.environ.get('WORKSHOP_VIDEO_FONT', '/System/Library/Fonts/STHeiti Light.ttc')
MONO_PATH = os.environ.get('WORKSHOP_VIDEO_MONO_FONT', '/System/Library/Fonts/Menlo.ttc')


def source(lesson: int, example: int):
    lesson_data = json.loads((ROOT / 'lessons' / f'{lesson:02}.json').read_text())
    return copy.deepcopy(lesson_data['examples'][example - 1])


def change(spec, old, new):
    result = copy.deepcopy(spec)
    if old not in result['code']:
        raise ValueError(f'Media variation target was not found: {old}')
    result['code'] = result['code'].replace(old, new)
    result.pop('expected', None)
    return result


def custom(code, files=None):
    return {'code': textwrap.dedent(code).strip(), 'files': files or {}}


def shot(title, caption, spec, note='', highlight=()):
    return {'title': title, 'caption': caption, 'spec': spec, 'note': note, 'highlight': list(highlight)}


def storyboards():
    notice1, notice2, notice3 = [source(1, n) for n in (1, 2, 3)]
    new_time = change(notice2, '周六 14:00', '周日 09:30')
    split_notice = change(notice3, 'puts -nonewline', 'puts')
    new_event = change(notice2, '周末读书会', '社区散步')
    loop1, loop2, loop3 = [source(5, n) for n in (1, 2, 3)]
    zero = change(loop1, '{18 21 -1 19 23}', '{18 21 0 19 23}')
    empty_loop = change(loop1, '{18 21 -1 19 23}', '{}')
    two_rounds = change(loop2, '$i <= 3', '$i <= 2')
    two_bad = change(loop3, '{12 15 31 18}', '{12 15 31 35}')
    continue_bad = change(two_bad, 'break', 'continue')
    text1, text2, text3 = [source(7, n) for n in (1, 2, 3)]
    other_email = change(text1, 'LI.MING@EXAMPLE.ORG', 'LI.MING@OTHER.ORG')
    empty_email = change(text1, '  LI.MING@EXAMPLE.ORG  ', '   ')
    only_semicolon = change(text3, 'split $raw ",;"', 'split $raw ";"')
    file1, file2, file3 = [source(11, n) for n in (1, 2, 3)]
    more_data = copy.deepcopy(file1); more_data['files']['readings.txt'] = '1.2\n1.4\n1.6\n1.8\n'; more_data.pop('expected', None)
    missing = custom('set ch [open missing.txt r]\nputs [read $ch]\nclose $ch')
    caught = custom('''
        if {[catch {open missing.txt r} message]} {
            puts "无法读取文件"
            puts $message
        }
    ''')
    file4 = copy.deepcopy(file3); file4['files']['readings.txt'] = '2.0\n4.0\n6.0\n'; file4.pop('expected', None)
    proc1, proc2, proc3 = [source(10, n) for n in (1, 2, 3)]
    zero_order = change(proc1, 'fee 3 12', 'fee 0 12')
    new_order = change(proc1, 'fee 2 8', 'fee 5 7')
    namespace_fee = source(13, 2)
    namespace_more = change(namespace_fee, 'fee 3', 'fee 4')
    sta1, sta2, sta3 = [source(17, n) for n in (1, 2, 3)]
    relaxed = change(sta1, 'set period 10.0', 'set period 12.0')
    boundary = change(sta1, '{8.2 10.8}', '{10.0 10.8}')
    all_pass = change(sta3, 'set period 10.0', 'set period 12.0')
    final_summary = source(18, 3)
    partial_summary = source(18, 2)
    return [
        {'unit': 1, 'title': '运行第一个 Tcl 脚本', 'lessons': [1], 'shots': [
            shot('把活动信息交给电脑', '本演示用真实 Tcl 解释器运行代码；右侧是实际标准输出。', notice1, '原始信息：周末读书会'),
            shot('一条命令，一个参数', 'puts 是命令名；双引号把活动文字组成一个完整参数。', notice1, highlight=(1,)),
            shot('把三项安排写成脚本', '脚本按顺序运行；每条 puts 默认在末尾换行。', notice2, '通知需要活动、时间和地点。'),
            shot('注释解释意图', '# 开始的独立注释行不会出现在标准输出中。', notice2, highlight=(1,)),
            shot('修改活动时间', '把周六下午改成周日上午，然后重新运行。', new_time, highlight=(3,)),
            shot('检查新的通知', '输出已经改变；不是按示例编号返回固定文字。', new_time, '核对时间：周日 09:30'),
            shot('两次输出放在一行', '-nonewline 让第一次输出不换行，第二次继续写在同一行。', notice3, highlight=(1,)),
            shot('删除选项，对照结果', '删掉 -nonewline 后，前缀和截止时间分成两行。', split_notice, '只改一个条件，观察实际变化。'),
            shot('读懂真实错误', 'puts 的参数数量错误会被解释器报告；此时不显示成功。', custom('puts "通知" # 说明'), '错误示例：# 位于参数位置。'),
            shot('把注释放到独立行', '修正注释写法，再运行，确认代码与输出都正确。', notice2),
            shot('换成自己的活动', '保留通知格式，替换活动名称即可复用脚本。', new_event, highlight=(2,)),
            shot('自己动手试一次', '把时间、地点换成自己的安排；保存为 notice.tcl 可在本地执行。', new_event, '本地命令：tclsh notice.tcl')
        ]},
        {'unit': 2, 'title': '使用循环处理列表', 'lessons': [5, 6], 'shots': [
            shot('一组测量，不逐条复制代码', '这组读数里，负数表示采集失败；有效读数需要累计。', loop1, '原始数据：18、21、-1、19、23'),
            shot('循环前初始化', 'count 与 total 从 0 开始；foreach 每轮取出一个元素。', loop1, highlight=(1, 2, 3)),
            shot('跳过失败读数', 'continue 跳过当前负值，后面的有效测量仍会继续处理。', loop1, highlight=(4,)),
            shot('零值也是一条测量', '把 -1 改为 0：总和相同，但有效次数增加。', zero, highlight=(3,)),
            shot('空输入不执行循环体', '把数据换成空列表：初始化的两个 0 就是结果。', empty_loop, highlight=(3,)),
            shot('有固定次数时使用 for', 'for 包含初始化、条件、更新、循环体四个参数。', loop2),
            shot('检查计数的边界', '把上界由 3 改成 2，输出也减少为两次。', two_rounds, highlight=(1,)),
            shot('while 每轮先检查条件', '待处理数量在循环体中递减，保证最终能够结束。', loop3, highlight=(2, 4)),
            shot('找到首个异常就停止', 'break 结束整个循环，只保留第一条超过阈值的读数。', two_bad, highlight=(9,)),
            shot('continue 与 break 不相同', '改为 continue 后，第二条异常也会被看到。', continue_bad, highlight=(9,)),
            shot('回到任务所需的规则', '需要首个异常时恢复 break；需要所有异常时继续遍历。', two_bad),
            shot('用新数据验证', '自己换一组含负数、零值的读数，再试空列表和阈值边界。', loop1, '不要只验证一组正常数据。')
        ]},
        {'unit': 3, 'title': '清理文本并观察结果', 'lessons': [7, 8, 9], 'shots': [
            shot('看清原始联系人文字', '原记录包含两端空格和大写字母；清理规则应明确。', text1, '尖括号帮助看见两端空格。'),
            shot('先 trim，再 tolower', '内层命令去掉两端空白；外层命令把结果转成小写。', text1, highlight=(2,)),
            shot('原值与新值分别保存', 'raw 保持原始数据；email 保存清理后的返回值。', text1, highlight=(3, 4)),
            shot('简单后缀检查', 'string match 的星号是通配符；这不是完整邮箱合法性验证。', text1, highlight=(5,)),
            shot('换一个域名', '改成 other.org 后，清理仍成功，但指定域名匹配返回 0。', other_email),
            shot('只有空白时会怎样', '空白清理成空字符串；不能把它误认为有效地址。', empty_email),
            shot('分隔文本转成列表', 'split 按分号切分；join 把列表用更可读的分隔文字连接。', text2, highlight=(2, 4)),
            shot('观察每个元素', 'llength 计算元素数，lindex 取出一个完整元素。', text2, highlight=(3, 5)),
            shot('连续分隔符产生空元素', '甲和乙之间的两个分号保留了一个空段，长度为 0。', text3, highlight=(2, 5)),
            shot('分隔参数是字符集合', '只按分号切分时，逗号仍留在同一个元素内部。', only_semicolon, highlight=(2,)),
            shot('不要删掉姓名内部的空格', 'trim 只清除两端空白，林和雨之间有意义的空格被保留。', text3, highlight=(6,)),
            shot('把清理规则写清楚', '接下来可以逐段清理并删除空项，再用字典整理多个字段。', text2, '用空输入、不同大小写和额外分隔符再测试。')
        ]},
        {'unit': 4, 'title': '读取文件与处理错误', 'lessons': [11, 12], 'shots': [
            shot('从教学文件读取记录', '本演示文件在临时目录里；网页对应浏览器虚拟文件，不能读取私人磁盘。', file1, '输入文件：readings.txt'),
            shot('打开、读取、关闭', 'open 返回通道；read 取出内容；close 释放文件资源。', file1, highlight=(1, 2, 3)),
            shot('换一份输入文件', '增加一行测量，再运行，标准输出显示新的文件内容。', more_data, '输入文件新增 1.8。'),
            shot('逐行读取与空白行', 'gets 返回读取到的字符数；空白行长度 0 仍然是一行。', file2, highlight=(3,)),
            shot('文件末尾的判断', '使用 gets >= 0 判断是否读到一行；不能把空白行当文件末尾。', file2, '开始、空白、结束：共三行。'),
            shot('缺失文件产生真实错误', 'open missing.txt 失败，解释器返回原因；流程没有继续读取。', missing, '当前目录没有 missing.txt。'),
            shot('用 catch 处理可预期问题', 'catch 返回错误状态，message 保存原因，再输出可理解的提示。', caught),
            shot('明确报告失败', '出现提示不等于文件读取成功；保留错误原因便于修正。', caught, '缺失文件仍然缺失。'),
            shot('生成一份摘要文件', '读取三个值，统计数量与平均数，把结果写入 summary.txt。', file3),
            shot('重新读取，验证写入', '摘要写入后关闭通道，再打开文件读取，核对实际保存内容。', file3, highlight=(11, 12, 13)),
            shot('修改输入，摘要随之变化', '把测量改成 2、4、6，平均数来自真正的计算。', file4),
            shot('在自己的环境复现', '复制代码与教学数据，用 tclsh 运行；浏览器文件不会自动写到本地磁盘。', file3, '需要文件时，先准备同名教学输入。')
        ]},
        {'unit': 5, 'title': '使用过程组织代码', 'lessons': [10, 13], 'shots': [
            shot('让计算接受不同输入', '过程把费用计算封装成一个可重复调用的工具。', proc1),
            shot('参数进入过程', 'quantity 和 price 是本次调用的输入；return 返回乘积。', proc1, highlight=(1, 2)),
            shot('同一份逻辑，两张订单', '调用 fee 3 12 和 fee 2 8；结果来自各自的参数。', proc1, highlight=(4, 5)),
            shot('验证零件数边界', '把第一张订单数量改为 0，返回费用 0。', zero_order),
            shot('再换一张订单', '数量 5、价格 7 也复用同一个过程，避免写死样例结果。', new_order),
            shot('为可选参数设置默认值', 'delivery 默认是 0；调用者也可以明确传入运费。', proc2, highlight=(1,)),
            shot('返回值交给格式化命令', '过程负责计算，format 负责把金额显示为两位小数。', proc2, highlight=(4, 5)),
            shot('局部变量与外部变量', '过程里的 subtotal 是局部变量，不覆盖外部同名变量。', proc3, highlight=(1, 3)),
            shot('明确传入，明确返回', '用参数和 return 传递数据，减少对隐藏全局状态的依赖。', proc3),
            shot('同名工具放入命名空间', 'travel::fee 与 food::fee 组织不同工具，名字不会冲突。', namespace_fee),
            shot('命名空间工具也接受新输入', '把人数从 3 改成 4，两种费用都重新计算。', namespace_more),
            shot('先用过程，再按需要组织', '小任务用过程已经足够；项目变大时再引入命名空间和脚本文件。', namespace_fee, '下一步：source 工具脚本，并传入命令行参数。')
        ]},
        {'unit': 6, 'title': '分析教学版 VLSI 报告', 'lessons': [17, 18], 'shots': [
            shot('先明确教学模型', '这里是原创教学路径数据；没有连接商业 EDA 软件。', sta1, '简化模型：slack = 周期 − 路径延迟'),
            shot('看懂正负 slack', '周期 10 ns：延迟小于周期时余量为正，大于周期时余量为负。', sta1, highlight=(1, 3)),
            shot('边界值也要检查', '路径延迟恰好等于周期时，教学 slack 为 0。', boundary),
            shot('改变周期，重新计算', '把周期改为 12 ns，同一组延迟的 slack 随真实运算变化。', relaxed),
            shot('从约定格式提取字段', 'regexp 从 PATH 名称和 DELAY 数值构造一条字典记录。', sta2),
            shot('先检查格式，再使用字段', '解析失败要报告错误；不能把无效行混进统计。', sta2, highlight=(2, 3)),
            shot('筛选负 slack', '遍历路径，只收集教学 slack 小于 0 的项。', sta3, highlight=(5,)),
            shot('按严重程度排序', '用数值排序把最负的 slack 放在前面，先关注最紧张的路径。', sta3, highlight=(7,)),
            shot('没有负 slack 的输入', '把周期改为 12 ns，筛选结果为空；空输出是有意义的结果。', all_pass),
            shot('组合多份文件', '第 18 节工具读取两份报告，自动生成路径数和最差 slack 摘要。', final_summary, 'report-tools.tcl 提供已验证的解析与统计过程。'),
            shot('坏报告明确列出', '坏文件不混入有效统计，输出清楚标注这是部分结果。', partial_summary),
            shot('把简化模型与真实 STA 分清', '真实 STA 还有时钟、建立保持、例外和工具模型；本演示用于学习 Tcl 数据流程。', final_summary, '输入 → 解析 → 统计 → 写出摘要')
        ]}
    ]


def fonts(size=24, mono=False):
    return ImageFont.truetype(MONO_PATH if mono else FONT_PATH, size)


def fit_lines(value, font, width):
    """Visual soft wrap only. The executed source string is never modified."""
    result = []
    for line in value.splitlines() or ['']:
        if not line:
            result.append(''); continue
        current = ''
        for character in line:
            if current and font.getlength(current + character) > width:
                result.append(current); current = character
            else:
                current += character
        result.append(current)
    return result


def draw_frame(unit, sequence, data, result):
    image = Image.new('RGB', (WIDTH, HEIGHT), '#faf7ef')
    d = ImageDraw.Draw(image)
    title_font, label_font, body_font = fonts(31), fonts(21), fonts(23)
    d.text((34, 24), 'Tcl 自动化工作坊', fill='#276960', font=label_font)
    d.text((34, 58), f'单元 {unit["unit"]} · {unit["title"]}', fill='#243c38', font=title_font)
    d.text((1115, 34), f'{sequence:02} / 12', fill='#607a71', font=label_font)
    d.line((34, 108, 1246, 108), fill='#adc3b8', width=2)
    d.text((34, 128), data['title'], fill='#243c38', font=fonts(27))
    d.rounded_rectangle((34, 172, 797, 602), 12, fill='#193b36')
    d.rounded_rectangle((817, 172, 1246, 602), 12, fill='#e4eeea', outline='#adc3b8', width=2)
    d.text((54, 190), '代码 · 源码仅视觉折行', fill='#b9d5c9', font=fonts(18))
    d.text((836, 190), f'真实 Tcl {result["version"]} · 执行结果', fill='#276960', font=fonts(18))
    codefont = fonts(21, True)
    code_lines = []
    for number, line in enumerate(data['spec']['code'].splitlines(), 1):
        wrapped = fit_lines(line, codefont, 705)
        code_lines.extend((number if index == 0 else None, text) for index, text in enumerate(wrapped))
    if len(code_lines) > 16:
        codefont = fonts(18, True); code_lines = []
        for number, line in enumerate(data['spec']['code'].splitlines(), 1):
            wrapped = fit_lines(line, codefont, 705)
            code_lines.extend((number if index == 0 else None, text) for index, text in enumerate(wrapped))
    line_height = 21 if len(code_lines) > 16 else 24
    if len(code_lines) * line_height > 367:
        raise ValueError(f'Source does not fit a frame: {unit["unit"]}/{sequence} has {len(code_lines)} visual lines')
    for row, (number, line) in enumerate(code_lines):
        y = 225 + row * line_height
        if number in data['highlight']:
            d.rounded_rectangle((45, y - 2, 786, y + line_height - 1), 3, fill='#31564b')
        if number is not None:
            d.text((49, y), f'{number:02}', font=fonts(17, True), fill='#aac4b8')
        else:
            d.text((61, y), '>', font=fonts(17, True), fill='#aac4b8')
        # Chinese comments use the bundled CJK system face; ASCII source uses Menlo.
        d.text((85, y), line, font=codefont if all(ord(x) < 128 for x in line) else fonts(codefont.size), fill='#f4f7ec')
    success = result['error'] is None
    status = '完成' if success else '解释器错误'
    d.text((836, 225), status, fill='#276960' if success else '#9f4d29', font=fonts(23))
    output = result['output'] or ('（无标准输出）' if success else '（执行中止）')
    if result['error']:
        output += '\n' + result['error']
    lines = fit_lines(output, body_font, 387)
    if len(lines) > 10:
        raise ValueError(f'Output does not fit frame: {unit["unit"]}/{sequence}')
    for row, line in enumerate(lines):
        d.text((836, 266 + row * 30), line, font=body_font, fill='#243c38')
    if data['note']:
        note_lines = fit_lines(data['note'], fonts(18), 386)
        for row, line in enumerate(note_lines[:3]):
            d.text((836, 514 + row * 23), line, font=fonts(18), fill='#607a71')
    d.rounded_rectangle((34, 618, 1246, 700), 11, fill='#fff0da')
    captions = fit_lines(data['caption'], fonts(25), 1170)
    if len(captions) > 2:
        raise ValueError(f'Caption needs more than two lines: {unit["unit"]}/{sequence}')
    for row, caption in enumerate(captions):
        d.text((53, 630 + row * 32), caption, fill='#573f2b', font=fonts(25))
    # A quiet progress bar uses geometry as well as text; no flashing or motion.
    d.rectangle((34, 706, 34 + int(1212 * sequence / 12), 709), fill='#276960')
    return image


def timecode(seconds):
    return f'{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}.000'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--encode', action='store_true', help='Encode MP4 with macOS Swift/AVFoundation')
    parser.add_argument('--unit', type=int, choices=range(1, 7))
    parser.add_argument('--frames-dir', type=Path, help='Keep the original PNG storyboard frames here')
    args = parser.parse_args()
    if not Path(FONT_PATH).is_file() or not Path(MONO_PATH).is_file():
        raise SystemExit('Font paths were not found. Set WORKSHOP_VIDEO_FONT and WORKSHOP_VIDEO_MONO_FONT to installed CJK and monospace fonts.')
    if args.encode and not shutil.which('swift'):
        raise SystemExit('MP4 encoding requires macOS Swift/AVFoundation; frame/subtitle generation also works without --encode.')
    MEDIA.mkdir(parents=True, exist_ok=True)
    records = []
    cache = {}
    with tempfile.TemporaryDirectory(prefix='tcl-workshop-video-') as temp:
        frame_root = args.frames_dir or Path(temp)
        for unit in storyboards():
            if args.unit and unit['unit'] != args.unit:
                continue
            folder = frame_root / f'unit-{unit["unit"]}'; folder.mkdir(parents=True, exist_ok=True)
            transcript = [f'单元 {unit["unit"]}：{unit["title"]}', '',
                '时长：60 秒。无声原创代码演示，中文字幕已嵌入画面。',
                '画面为脚本生成的代码工作台，不是浏览器点击操作录像。',
                '所有代码均由真实本地 Tcl 解释器执行；标准输出与错误直接取自执行结果。',
                '每个镜头都在新临时目录和新解释器中执行；教学文件随镜头预置。',
                '源码只有显示折行，执行内容没有改变。文件操作不会访问私人数据。', '']
            vtt = ['WEBVTT', '']
            executions = []
            for sequence, data in enumerate(unit['shots'], 1):
                key = json.dumps(data['spec'], ensure_ascii=False, sort_keys=True)
                if key not in cache:
                    result = native(data['spec'])
                    if 'expected' in data['spec'] and (result['error'] or result['output'] != data['spec']['expected']):
                        raise ValueError(f'Course example changed: {unit["unit"]}/{sequence}: {result}')
                    cache[key] = result
                result = cache[key]
                begin, end = (sequence - 1) * HOLD, sequence * HOLD
                frame = draw_frame(unit, sequence, data, result)
                frame.save(folder / f'shot-{sequence:02}.png', optimize=True)
                if sequence == 1:
                    frame.save(MEDIA / f'unit-{unit["unit"]}.png', optimize=True)
                vtt.extend([str(sequence), f'{timecode(begin)} --> {timecode(end)}', data['caption'], ''])
                transcript.extend([f'[{timecode(begin)}–{timecode(end)}] {data["title"]}', data['caption']])
                if data['note']:
                    transcript.append('说明：' + data['note'])
                transcript.extend(['代码：', data['spec']['code'], f'真实 Tcl {result["version"]} 标准输出：', result['output'] or '（无标准输出）'])
                if result['error']:
                    transcript.extend(['真实解释器错误：', result['error']])
                for name, contents in data['spec'].get('files', {}).items():
                    transcript.extend([f'输入教学文件 {name}：', contents.rstrip('\n')])
                transcript.append('')
                executions.append({'shot': sequence, 'source_sha256': hashlib.sha256(data['spec']['code'].encode()).hexdigest(), 'version': result['version'], 'output': result['output'], 'error': result['error']})
            (MEDIA / f'unit-{unit["unit"]}.vtt').write_text('\n'.join(vtt), encoding='utf-8')
            (MEDIA / f'unit-{unit["unit"]}.txt').write_text('\n'.join(transcript), encoding='utf-8')
            record = {'unit': unit['unit'], 'title': unit['title'], 'seconds': HOLD * len(unit['shots']), 'shots': executions}
            if args.encode:
                completed = subprocess.run(['swift', '-suppress-warnings', '-module-cache-path', str(Path(temp) / 'swift-cache'), str(ROOT / 'scripts' / 'encode_video.swift'), str(folder), str(MEDIA / f'unit-{unit["unit"]}.mp4'), str(WIDTH), str(HEIGHT), str(FPS), str(HOLD)], text=True, capture_output=True, timeout=180)
                if completed.returncode:
                    raise RuntimeError('Native video encoding failed: ' + completed.stderr.strip())
                record['video'] = json.loads(completed.stdout.strip().splitlines()[-1])
                print(json.dumps(record['video'], ensure_ascii=False), flush=True)
            else:
                print(f'Unit {unit["unit"]}: frames, cover, subtitles and transcript ready; use --encode for video.', flush=True)
            records.append(record)
    # This report binds visible output and code hashes to the real execution version.
    (MEDIA / 'generation-report.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Rendered {len(records)} units; {len(cache)} unique native Tcl executions.', flush=True)


if __name__ == '__main__':
    main()
