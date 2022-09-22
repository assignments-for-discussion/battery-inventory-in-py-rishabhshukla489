def count_batteries_by_usage(cycles):
  low =0
  medium=0
  high =0
  for cycle in cycles:
    if cycle <410:
      low=low+1
    elif cycle>410 and cycle<909:
      medium=medium+1
    elif cycle>909:
      high=high+1
  return {
    "lowCount": low,
    "mediumCount": medium,
    "highCount": high
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  assert(counts["lowCount"] == 2)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
