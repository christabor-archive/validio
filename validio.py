import urllib2


def check_words(filename=None, output_file=False, throttle=False, throttle_amount=0):
    if filename is None:
        return

    if output_file:
        import time
        output = open('output.txt', 'w+')

    available = []

    with open(filename) as words:
        for word in words:
            word = word.strip()
            print 'Checking', word

            # throttle requests by one second
            if throttle:
                time.sleep(throttle_amount)

            try:
                # try to open url, specify a 1 second timeout
                web_url = 'http://' + word + '.io'
                urllib2.urlopen(web_url, None, 1000)
                available.append(word)
                print 'success! ==============='
                print word + '.io exists'
                print '========================'

                if output_file:
                    output.write('Valid url: ' + word + '.io \n')

            except urllib2.URLError:
                print 'Error: no url with that name exists'

                if output_file:
                    output.write('Invalid url: ' + word + '.io \n')

            finally:
                pass

        print 'Total domains that exist', available

        if output_file:
            output.close()

    return
