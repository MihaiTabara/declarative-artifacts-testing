import json
import pprint

FENNEC_MAPPING = {
    'aarch64': 'beetmover-android-aarch64-nightly/opt',
    'api16': 'beetmover-android-api-16-nightly/opt',
    'x86': 'beetmover-android-x86-nightly/opt',
    'x86_64': 'beetmover-android-x86_64-nightly/opt',
    'checksums_aarch64': 'beetmover-checksums-android-aarch64-nightly/opt',
    'checksums_api16': 'beetmover-checksums-android-api-16-nightly/opt',
    'checksums_x86_64': 'beetmover-checksums-android-x86_64-nightly/opt',
    'checksums_x86': 'beetmover-checksums-android-x86-nightly/opt',
    'source': 'beetmover-source-fennec-source/opt',
    'source_checksums': 'release-beetmover-source-checksums-fennec-source/opt',
    'generate_checksums': 'release-generate-checksums-fennec-beetmover',
}

FIREFOX_NIGHTLY_MAPPING = {
    'input_nightly_repackage_linux_with_partials': 'beetmover-repackage-linux-nightly/opt',
    'input_nightly_repackage_linux64_with_partials': 'beetmover-repackage-linux64-nightly/opt',
    'input_nightly_repackage_macosx64_with_partials': 'beetmover-repackage-macosx64-nightly/opt',
    'input_nightly_repackage_win32_with_partials': 'beetmover-repackage-win32-nightly/opt',
    'input_nightly_repackage_win64_with_partials': 'beetmover-repackage-win64-nightly/opt',
    'input_nightly_repackage_win64_aarch64_with_partials': 'beetmover-repackage-win64-aarch64-nightly/opt',
    'input_nightly_repackage_ach_linux_with_partials': 'beetmover-repackage-ach-linux-nightly/opt',
    'input_nightly_repackage_ach_linux64_with_partials': 'beetmover-repackage-ach-linux64-nightly/opt',
    'input_nightly_repackage_ach_macosx64_with_partials': 'beetmover-repackage-ach-macosx64-nightly/opt',
    'input_nightly_repackage_ach_win32_with_partials': 'beetmover-repackage-ach-win32-nightly/opt',
    'input_nightly_repackage_ach_win64_with_partials': 'beetmover-repackage-ach-win64-nightly/opt',
    'input_nightly_repackage_linux64_asan_with_partials': 'beetmover-repackage-linux64-asan-reporter-nightly/opt',
    'input_nightly_repackage_win64_asan_with_partials': 'beetmover-repackage-win64-asan-reporter-nightly/opt',
    'input_nightly_checksums_linux': 'beetmover-checksums-linux-nightly/opt',
    'input_nightly_checksums_linux64': 'beetmover-checksums-linux64-nightly/opt',
    'input_nightly_checksums_macosx64': 'beetmover-checksums-macosx64-nightly/opt',
    'input_nightly_checksums_win32': 'beetmover-checksums-win32-nightly/opt',
    'input_nightly_checksums_win64': 'beetmover-checksums-win64-nightly/opt',
    'input_nightly_checksums_win64_aarch64': 'beetmover-checksums-win64-aarch64-nightly/opt',
    'input_nightly_checksums_ach_linux': 'beetmover-checksums-ach-linux-nightly/opt',
    'input_nightly_checksums_ach_linux64': 'beetmover-checksums-ach-linux64-nightly/opt',
    'input_nightly_checksums_ach_macosx64': 'beetmover-checksums-ach-macosx64-nightly/opt',
    'input_nightly_checksums_ach_win32': 'beetmover-checksums-ach-win32-nightly/opt',
    'input_nightly_checksums_ach_win64': 'beetmover-checksums-ach-win64-nightly/opt',
    'input_nightly_checksums_ach_win64_aarch64': 'beetmover-checksums-ach-win64-aarch64-nightly/opt',
    'input_nightly_checksums_linux64_asan': 'beetmover-checksums-linux64-asan-reporter-nightly/opt',
    'input_nightly_checksums_win64_asan': 'beetmover-checksums-win64-asan-reporter-nightly/opt',
    # FIXME:
    'input_nightly_repackage_ach_win64_aarch64_with_partials': 'beetmover-repackage-ach-win64-aarch64-nightly/opt',
}

FIREFOX_BETA_MAPPING = {
    'input_beta_firefox_checksums_ach_linux': 'beetmover-checksums-ach-linux-nightly/opt',
    'input_beta_firefox_checksums_ach_linux64': 'beetmover-checksums-ach-linux64-nightly/opt',
    'input_beta_firefox_checksums_ach_macosx64': 'beetmover-checksums-ach-macosx64-nightly/opt',
    'input_beta_firefox_checksums_ach_win32': 'beetmover-checksums-ach-win32-nightly/opt',
    'input_beta_firefox_checksums_ach_win64': 'beetmover-checksums-ach-win64-nightly/opt',
    'input_beta_firefox_checksums_ach_win64_aarch64': 'beetmover-checksums-ach-win64-aarch64-nightly/opt',
    'input_beta_firefox_checksums_linux': 'beetmover-checksums-linux-nightly/opt',
    'input_beta_firefox_checksums_linux64': 'beetmover-checksums-linux64-nightly/opt',
    'input_beta_firefox_checksums_macosx64': 'beetmover-checksums-macosx64-nightly/opt',
    'input_beta_firefox_checksums_win32': 'beetmover-checksums-win32-nightly/opt',
    'input_beta_firefox_checksums_win64': 'beetmover-checksums-win64-nightly/opt',
    'input_beta_firefox_checksums_win64_aarch64': 'beetmover-checksums-win64-aarch64-nightly/opt',
    'input_beta_firefox_repackage_ach_linux': 'beetmover-repackage-ach-linux-nightly/opt',
    'input_beta_firefox_repackage_ach_linux64': 'beetmover-repackage-ach-linux64-nightly/opt',
    'input_beta_firefox_repackage_ach_macosx64': 'beetmover-repackage-ach-macosx64-nightly/opt',
    'input_beta_firefox_repackage_ach_win32': 'beetmover-repackage-ach-win32-nightly/opt',
    'input_beta_firefox_repackage_ach_win64': 'beetmover-repackage-ach-win64-nightly/opt',
    'input_beta_firefox_repackage_ach_win64_aarch64': 'beetmover-repackage-ach-win64-aarch64-nightly/opt',
    'input_beta_firefox_repackage_linux': 'beetmover-repackage-linux-nightly/opt',
    'input_beta_firefox_repackage_linux64': 'beetmover-repackage-linux64-nightly/opt',
    'input_beta_firefox_repackage_macosx64': 'beetmover-repackage-macosx64-nightly/opt',
    'input_beta_firefox_repackage_win32': 'beetmover-repackage-win32-nightly/opt',
    'input_beta_firefox_repackage_win64': 'beetmover-repackage-win64-nightly/opt',
    'input_beta_firefox_repackage_win64_aarch64': 'beetmover-repackage-win64-aarch64-nightly/opt',
    'input_beta_firefox_source': 'beetmover-source-firefox-source/opt',
    'input_beta_firefox_source_checksums': 'release-beetmover-source-checksums-firefox-source/opt',
    'input_beta_firefox_generate_checksums': 'release-generate-checksums-firefox-beetmover',
    'input_beta_firefox_siged_langpacks_linux': 'beetmover-signed-langpacks-build-linux-nightly/opt',
    'input_beta_firefox_siged_langpacks_linux64': 'beetmover-signed-langpacks-build-linux64-nightly/opt',
    'input_beta_firefox_siged_langpacks_macosx64': 'beetmover-signed-langpacks-build-macosx64-nightly/opt',
    'input_beta_firefox_siged_langpacks_win32': 'beetmover-signed-langpacks-build-win32-nightly/opt',
    'input_beta_firefox_siged_langpacks_win64': 'beetmover-signed-langpacks-build-win64-nightly/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_linux': 'beetmover-signed-langpacks-nightly-l10n-linux-nightly-1/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_linux64': 'beetmover-signed-langpacks-nightly-l10n-linux64-nightly-1/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_macosx64': 'beetmover-signed-langpacks-nightly-l10n-macosx64-nightly-1/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_macosx64': 'beetmover-signed-langpacks-nightly-l10n-macosx64-nightly-1/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_macosx64_ja_JP': 'beetmover-signed-langpacks-nightly-l10n-macosx64-nightly-ja-JP-mac/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_win32': 'beetmover-signed-langpacks-nightly-l10n-win32-nightly-1/opt',
    'input_beta_firefox_siged_langpacks_nightly_l10n_win64': 'beetmover-signed-langpacks-nightly-l10n-win64-nightly-1/opt',
    'input_beta_firefox_signed_langpacks_checksums_linux': 'release-beetmover-signed-langpacks-checksums-linux/opt',
    'input_beta_firefox_signed_langpacks_checksums_linux64': 'release-beetmover-signed-langpacks-checksums-linux64/opt',
    'input_beta_firefox_signed_langpacks_checksums_macosx64': 'release-beetmover-signed-langpacks-checksums-macosx64/opt',
    'input_beta_firefox_signed_langpacks_checksums_win32': 'release-beetmover-signed-langpacks-checksums-win32/opt',
    'input_beta_firefox_signed_langpacks_checksums_win64': 'release-beetmover-signed-langpacks-checksums-win64/opt',
    'input_beta_firefox_signed_langpacks_checksums_l10n_linux': 'release-beetmover-signed-langpacks-checksums-linux-1/opt',
    'input_beta_firefox_signed_langpacks_checksums_l10n_linux64': 'release-beetmover-signed-langpacks-checksums-linux64-1/opt',
    'input_beta_firefox_signed_langpacks_checksums_l10n_macosx64': 'release-beetmover-signed-langpacks-checksums-macosx64-1/opt',
    'input_beta_firefox_signed_langpacks_checksums_l10n_win32': 'release-beetmover-signed-langpacks-checksums-win32-1/opt',
    'input_beta_firefox_signed_langpacks_checksums_l10n_win64': 'release-beetmover-signed-langpacks-checksums-win64-1/opt',
}

DEVEDITION_BETA_MAPPING = {
    'input_beta_devedition_checksums_ach_linux': 'beetmover-checksums-ach-linux-devedition-nightly/opt',
    'input_beta_devedition_checksums_ach_linux64': 'beetmover-checksums-ach-linux64-devedition-nightly/opt',
    'input_beta_devedition_checksums_ach_macosx': 'beetmover-checksums-ach-macosx64-devedition-nightly/opt',
    'input_beta_devedition_checksums_ach_win32': 'beetmover-checksums-ach-win32-devedition-nightly/opt',
    'input_beta_devedition_checksums_ach_win64aarch64': 'beetmover-checksums-ach-win64-aarch64-devedition-nightly/opt',
    'input_beta_devedition_checksums_ach_win64': 'beetmover-checksums-ach-win64-devedition-nightly/opt',
    'input_beta_devedition_checksums_linux': 'beetmover-checksums-linux-devedition-nightly/opt',
    'input_beta_devedition_checksums_linux64': 'beetmover-checksums-linux64-devedition-nightly/opt',
    'input_beta_devedition_checksums_macosx': 'beetmover-checksums-macosx64-devedition-nightly/opt',
    'input_beta_devedition_checksums_win32': 'beetmover-checksums-win32-devedition-nightly/opt',
    'input_beta_devedition_checksums_win64aarch64': 'beetmover-checksums-win64-aarch64-devedition-nightly/opt',
    'input_beta_devedition_checksums_win64': 'beetmover-checksums-win64-devedition-nightly/opt',
    'input_beta_devedition_repackage_ach_linux': 'beetmover-repackage-ach-linux-devedition-nightly/opt',
    'input_beta_devedition_repackage_ach_linux64': 'beetmover-repackage-ach-linux64-devedition-nightly/opt',
    'input_beta_devedition_repackage_ach_macosx': 'beetmover-repackage-ach-macosx64-devedition-nightly/opt',
    'input_beta_devedition_repackage_ach_win32': 'beetmover-repackage-ach-win32-devedition-nightly/opt',
    'input_beta_devedition_repackage_ach_win64aarch64': 'beetmover-repackage-ach-win64-aarch64-devedition-nightly/opt',
    'input_beta_devedition_repackage_ach_win64': 'beetmover-repackage-ach-win64-devedition-nightly/opt',
    'input_beta_devedition_repackage_linux': 'beetmover-repackage-linux-devedition-nightly/opt',
    'input_beta_devedition_repackage_linux64': 'beetmover-repackage-linux64-devedition-nightly/opt',
    'input_beta_devedition_repackage_macosx': 'beetmover-repackage-macosx64-devedition-nightly/opt',
    'input_beta_devedition_repackage_win32': 'beetmover-repackage-win32-devedition-nightly/opt',
    'input_beta_devedition_repackage_win64aarch64': 'beetmover-repackage-win64-aarch64-devedition-nightly/opt',
    'input_beta_devedition_repackage_win64': 'beetmover-repackage-win64-devedition-nightly/opt',
    'input_beta_devedition_source': 'beetmover-source-devedition-source/opt',
    'input_beta_devedition_source_checksums': 'release-beetmover-source-checksums-devedition-source/opt',
    'input_beta_devedition_generate_checksums': 'release-generate-checksums-devedition-beetmover',
    'input_beta_devedition_signed_langpacks_linux': 'release-beetmover-signed-langpacks-linux-devedition-nightly/opt',
    'input_beta_devedition_signed_langpacks_l10n_linux': 'release-beetmover-signed-langpacks-linux-devedition-nightly-1/opt',
    'input_beta_devedition_signed_langpacks_macosx': 'release-beetmover-signed-langpacks-macosx64-devedition-nightly/opt',
    'input_beta_devedition_signed_langpacks_l10n_macosx': 'release-beetmover-signed-langpacks-macosx64-devedition-nightly-1/opt',
    'input_beta_devedition_signed_langpacks_win32': 'release-beetmover-signed-langpacks-win32-devedition-nightly/opt',
    'input_beta_devedition_signed_langpacks_l10n_win32': 'release-beetmover-signed-langpacks-win32-devedition-nightly-1/opt',
    'input_beta_devedition_signed_langpacks_win64': 'release-beetmover-signed-langpacks-win64-devedition-nightly/opt',
    'input_beta_devedition_signed_langpacks_l10n_win64': 'release-beetmover-signed-langpacks-win64-devedition-nightly-1/opt',
    'input_beta_devedition_signed_langpacks_linux_checksums': 'release-beetmover-signed-langpacks-checksums-linux-devedition/opt',
    'input_beta_devedition_signed_langpacks_linux_l10n_checksums': 'release-beetmover-signed-langpacks-checksums-linux-devedition-1/opt',
    'input_beta_devedition_signed_langpacks_macosx_checksums': 'release-beetmover-signed-langpacks-checksums-macosx64-devedition/opt',
    'input_beta_devedition_signed_langpacks_macosx_l10n_checksums': 'release-beetmover-signed-langpacks-checksums-macosx64-devedition-1/opt',
    'input_beta_devedition_signed_langpacks_win32_checksums': 'release-beetmover-signed-langpacks-checksums-win32-devedition/opt',
    'input_beta_devedition_signed_langpacks_win32_l10n_checksums': 'release-beetmover-signed-langpacks-checksums-win32-devedition-1/opt',
    'input_beta_devedition_signed_langpacks_win64_checksums': 'release-beetmover-signed-langpacks-checksums-win64-devedition/opt',
    'input_beta_devedition_signed_langpacks_win64_l10n_checksums': 'release-beetmover-signed-langpacks-checksums-win64-devedition-1/opt',
}


def process_beetmover_log(input_filename):
    with open(input_filename, 'r') as f:
        raw_lines = f.readlines()
        lines = [raw_line.split(': ') for raw_line in raw_lines]
        di = dict((line[0], line[1].rstrip()) for line in lines)
        di = {}
        for line in lines:
            path = line[0]
            # FIXME: to optimize this per-product
            destination = line[1].replace('s3://net-mozaws-prod-delivery-archive/', '')
            if path in di.keys():
                di[path].append(destination.rstrip())
            else:
                di[path] = [destination.rstrip()]

        return di

def process_da_output(bm_job):
    # FIXME: to optimize this to read it from cmd args
    with open("/Users/mtabara/work/mozilla/clones/hg/dirty_devedition_70.0b4.json", "r") as f:
        data = json.loads(f.read())
        artifactMap = data[bm_job]['task']['payload']['artifactMap']

    di = {}
    for artifact in artifactMap:
        for path, config in artifact['paths'].items():
            # XXX: until I understand why target.bz2.complete.mar is unused,
            # hack this to be ignored
            if 'target.bz2.complete.mar' in path:
                continue
            if path in di:
                di[path].extend(config['destinations'])
            else:
                di[path] = config['destinations']
    return di


if __name__=='__main__':
    for filename, beetmover_job in DEVEDITION_BETA_MAPPING.items():
        bm_d = process_beetmover_log('{}.log'.format(filename))
        da_d = process_da_output(beetmover_job)

        print('=================== Comparing for {}'.format(filename))
        if bm_d.keys() != da_d.keys():
            import pdb; pdb.set_trace()
            assert len(bm_d.keys()) == len(da_d.keys()), "Size is different!"
            print("Same size, but turns out content doesn't match ...")
            print('BM {}'.format(sorted(bm_d.keys())))
            print('DA {}'.format(sorted(da_d.keys())))
            assert sorted(bm_d.keys()) == sorted(da_d.keys()), "Keys are different"

        for path, destinations in bm_d.items():
            if sorted(da_d[path]) != sorted(destinations):
                print("--- Destinations don't match.\nBM has {}\n DA has{}\n"
                    "".format(sorted(destinations), sorted(da_d[path])))
            else:
                print ("+++ Contents match for {}".format(path))

        print('=================')
