import pytest

from pharmpy.config import ConfigurationContext
from pharmpy.model import Parameter, Parameters
from pharmpy.plugins.nonmem import conf


@pytest.mark.usefixtures('parser')
@pytest.mark.parametrize(
    'buf,comment,expected',
    [
        ('$THETA 0', False, [('THETA(1)', 0, -1000000, 1000000, False)]),
        ('$THETA (0,1,INF)', False, [('THETA(1)', 1, 0, 1000000, False)]),
        ('$THETA    12.3 \n\n', False, [('THETA(1)', 12.3, -1000000, 1000000, False)]),
        ('$THETA  (0,0.00469) ; CL', False, [('THETA(1)', 0.00469, 0, 1000000, False)]),
        (
            '$THETA  (0,3) 2 FIXED (0,.6,1) 10 (-INF,-2.7,0)  (37 FIXED)\n 19 (0,1,2)x3',
            False,
            [
                ('THETA(1)', 3, 0, 1000000, False),
                ('THETA(2)', 2, -1000000, 1000000, True),
                ('THETA(3)', 0.6, 0, 1, False),
                ('THETA(4)', 10, -1000000, 1000000, False),
                ('THETA(5)', -2.7, -1000000, 0, False),
                ('THETA(6)', 37, -1000000, 1000000, True),
                ('THETA(7)', 19, -1000000, 1000000, False),
                ('THETA(8)', 1, 0, 2, False),
                ('THETA(9)', 1, 0, 2, False),
                ('THETA(10)', 1, 0, 2, False),
            ],
        ),
        (
            '$THETA (0.00469555) FIX ; CL',
            False,
            [('THETA(1)', 0.00469555, -1000000, 1000000, True)],
        ),
        (
            '$THETA\n ;; Model characteristics\n (0, 0.15, 0.6) ; Proportional\n',
            False,
            [('THETA(1)', 0.15, 0, 0.6, False)],
        ),
        ('$THETA\n;\n1;COMMENTING', False, [('THETA(1)', 1, -1000000, 1000000, False)]),
        (
            '$THETA\n   ;CMT1;SAMELINE\n;ONLYCOMMENT\n\t;COMMENT2\n    1    \n',
            False,
            [('THETA(1)', 1, -1000000, 1000000, False)],
        ),
        (
            '$THETA\n ;; Model characteristics\n  (0, 0.15, 0.6) ; Proportional error (Drug123)\n'
            '  (0, 1, 10)     ; Additive error (Drug123)\n',
            False,
            [('THETA(1)', 0.15, 0, 0.6, False), ('THETA(2)', 1, 0, 10, False)],
        ),
        ('$THETA  (FIX FIX 0.4) ; CL', False, [('THETA(1)', 0.4, -1000000, 1000000, True)]),
        ('$THETA (FIX 1,   FIX FIX    1 FIX, 1  FIX) ; CL', False, [('THETA(1)', 1, 1, 1, True)]),
        (
            '$THETA\n(0,0.105,)   ; RUV_CVFPG\n',
            False,
            [
                ('THETA(1)', 0.105, 0, 1000000, False),
            ],
        ),
        (
            '$THETA\n(0,0.105,)   ; RUV_CVFPG\n',
            True,
            [
                ('RUV_CVFPG', 0.105, 0, 1000000, False),
            ],
        ),
        (
            '$THETA  (0,3) ; CL\n 2 FIXED ; V\n',
            True,
            [
                ('CL', 3, 0, 1000000, False),
                ('V', 2, -1000000, 1000000, True),
            ],
        ),
    ],
)
def test_parameters(parser, buf, comment, expected):
    opt = ['comment', 'basic'] if comment else ['basic']
    with ConfigurationContext(conf, parameter_names=opt):
        recs = parser.parse(buf)
        rec = recs.records[0]
        pset = Parameters.create(rec.parameters(1))
        assert pset == Parameters.create([Parameter(*res) for res in expected])

        assert len(pset) == len(rec)


def test_theta_num(parser):
    rec = parser.parse('$THETA 1').records[0]
    pset = Parameters.create(rec.parameters(2))
    assert len(pset) == 1
    assert pset['THETA(2)'].init == 1


def test_update(parser):
    rec = parser.parse('$THETA 1').records[0]
    rec.parameters(1)
    pset = Parameters((Parameter('THETA(1)', 41),))
    rec.update(pset, 1)
    assert str(rec) == '$THETA 41'

    rec = parser.parse('$THETA 1 FIX').records[0]
    rec.parameters(1)
    pset = Parameters((Parameter('THETA(1)', 1, fix=False),))
    rec.update(pset, 1)
    assert str(rec) == '$THETA 1'

    rec = parser.parse('$THETA (2, 2, 2)  FIX').records[0]
    rec.parameters(1)
    pset = Parameters((Parameter('THETA(1)', 2, lower=2, upper=2, fix=False),))
    rec.update(pset, 1)
    assert str(rec) == '$THETA (2, 2, 2)'

    rec = parser.parse('$THETA (2, 2, 2 FIX)').records[0]
    rec.parameters(1)
    pset = Parameters((Parameter('THETA(1)', 2, lower=2, upper=2, fix=False),))
    rec.update(pset, 1)
    assert str(rec) == '$THETA (2, 2, 2)'

    rec = parser.parse('$THETA (2, 2, 2)').records[0]
    rec.parameters(1)
    pset = Parameters((Parameter('THETA(1)', 2, lower=2, upper=2, fix=True),))
    rec.update(pset, 1)
    assert str(rec) == '$THETA (2, 2, 2) FIX'

    rec = parser.parse('$THETA 1 2 3 ;CMT').records[0]
    rec.parameters(1)
    pset = Parameters(
        (
            Parameter('THETA(1)', 1, fix=True),
            Parameter('THETA(2)', 2),
            Parameter('THETA(3)', 3, fix=True),
        )
    )
    rec.update(pset, 1)
    assert str(rec) == '$THETA 1 FIX 2 3 FIX ;CMT'


@pytest.mark.usefixtures('parser')
@pytest.mark.parametrize(
    'buf,name_original,theta_number,buf_new',
    [
        ('$THETA 0', 'TVCL', 1, '$THETA 0 ; TVCL\n'),
    ],
)
def test_add_nonmem_name(parser, buf, name_original, theta_number, buf_new):
    rec = parser.parse(buf).records[0]
    rec.add_nonmem_name(name_original, theta_number)

    assert str(rec) == buf_new
    assert rec.name_map[name_original] == theta_number


def test_remove_theta(parser):
    rec = parser.parse('$THETA 1 2 3 ;CMT').records[0]
    rec.parameters(1)
    rec.remove(['THETA(1)', 'THETA(3)'])
    assert str(rec) == '$THETA  2  ;CMT'
