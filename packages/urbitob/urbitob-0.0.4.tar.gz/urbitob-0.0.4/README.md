# urbit-pob

A python implementation of [urbit-ob](https://github.com/urbit/urbit-ob)

### Install

Run `pip install urbitob`

### Module Use

The library exposes two families of functions:

* `patp / patp_to_num / patp_to_hex / hex_to_patp / is_valid_patp`
* `patq / patq_to_num / patq_to_hex / hex_to_patq / is_valid_patq`

As well as:

* `clan`, for determining the ship class of a `@p` value
* `sein`, for determining the parent of a `@p` value
* `eq_patq`, for comparing `@q` values for equality
* `is_valid_pat`, for a faster/weaker check of `@p` or `@q`-ness that only
  validates syllables (and not proper dash formatting)

### Example Usage

```py
>>> import urbitob
>>> urbitob.patp(314159)
'~batdyr-topmun'
>>> urbitob.patp_to_num("~faster-pollen")
2077885931
>>> urbitob.hex_to_patq("EFFACED")
'~wisfes-batsed'
>>> urbitob.sein("~hashes-happen")
'~hattug'
>>> urbitob.clan("~marzod")
'star'
```

You could use it to generate list of Planets from a given Star:
```py
>>> v = urbitob.patq_to_hex("~sordem")
>>> planets = list(urbitob.hex_to_patp(hex(i)[2:]+v) for i in range(1,0xffff))
>>> planets[:10]
['~rigteg-havtuc', '~lonnub-navhet', '~risheb-difryc', '~sigren-daldux', '~rammel-malmyl', '~rapmes-ralres', '~boswex-ravret', '~sapper-loclut', '~talmep-sibsug', '~dalbur-todser']
```

### Testing

A simple `python -m unittest` will run the test suite.
