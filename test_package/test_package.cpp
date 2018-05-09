#include <elfio/elfio_dump.hpp>
#include <iostream>

using namespace ELFIO;

int main( int argc, char** argv )
{
    elfio reader;

    if ( !reader.load( argv[0] ) ) {
        std::cerr << argv[0] << " is not an ELF file\n";
        return 1;
    }

    dump::header         ( std::cout, reader );
    dump::section_headers( std::cout, reader );
    dump::segment_headers( std::cout, reader );
    dump::symbol_tables  ( std::cout, reader );
    dump::notes          ( std::cout, reader );
    dump::dynamic_tags   ( std::cout, reader );
    dump::section_datas  ( std::cout, reader );
    dump::segment_datas  ( std::cout, reader );

    return 0;
}
