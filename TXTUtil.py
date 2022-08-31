import os
import time


def mksubfile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    with open(filename, 'w', encoding='utf-8') as fout:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1


def split_by_line_count(filename, count):
    with open(filename, 'r', encoding='utf-8') as fin:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mksubfile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mksubfile(buf, head, filename, sub)


if __name__ == '__main__':
    begin = time.time()
    split_by_line_count('F:/workdata/workdata.txt', 200000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))
