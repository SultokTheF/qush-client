import React, { useState, useEffect } from 'react';

import '../assets/styles/FieldList.css';

import FieldHandler from '../../../services/FieldHandler';
import Field from '../../../types/Field';

import FieldCard from '../../../components/layouts/FieldCard';

import Spinner from '../../../components/ui/Spinner';

const InfiniteFieldList: React.FC = () => {
  const [fields, setFields] = useState<Field[]>();
  
  useEffect(() => {
    fetchFieldList();
  }, []);

  const fetchFieldList = async () => {
    try {
      const fieldsData = await FieldHandler.fetchFields();
      setFields(fieldsData);
    } catch (error) {
      console.error('Error fetching fields:', error);
    }
  };
  
  return (
    <>
      <div>
        <section className='offer section container'>
          <div className="secContainter">

            <div className="secIntro">
              <h2 className='secTitle text-light'>
                Все доступные предложения
              </h2>
              <p className='text-light'>
                Здесь предствлены все спортивные поля, доступные на данный момент
              </p>

            </div>

            { fields? (
              <div className="mainContent grid">
              {fields.map(field => (
                <FieldCard key={field.id} field={field}/>
              ))}
            </div>
            ) : (
              <Spinner/>
            ) }
          </div>
        </section>
      </div>
    </>
  );
}

export default InfiniteFieldList;